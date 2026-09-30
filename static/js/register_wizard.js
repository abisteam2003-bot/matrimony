/**
 * Matromani 8-Step Registration Wizard Controller
 * Handles Multi-Step State, Autosave, Resume, Income Category Engine, and Form Validation
 */

let currentStep = 1;
const totalSteps = 8;
let formDataCache = {};
let autosaveTimeout = null;

document.addEventListener('DOMContentLoaded', async function () {
    initWizard();
    setupIncomeCalculator();
    setupPhotoPreviews();
    await checkResumeData();
});

function initWizard() {
    updateStepUI(currentStep);

    // Step Indicator Click (only allows moving to visited or completed steps)
    document.querySelectorAll('.step-indicator-item').forEach(item => {
        item.addEventListener('click', function () {
            const targetStep = parseInt(this.getAttribute('data-step'));
            if (targetStep < currentStep || this.classList.contains('completed')) {
                goToStep(targetStep);
            }
        });
    });

    // Next Step Buttons
    document.querySelectorAll('.btn-wizard-next').forEach(btn => {
        btn.addEventListener('click', async function (e) {
            e.preventDefault();
            const step = parseInt(this.getAttribute('data-step'));
            await handleStepSubmit(step);
        });
    });

    // Previous Step Buttons
    document.querySelectorAll('.btn-wizard-prev').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const prevStep = parseInt(this.getAttribute('data-step'));
            goToStep(prevStep);
        });
    });

    // Final Submit Button (Step 8)
    const finalSubmitBtn = document.getElementById('btn-final-submit');
    if (finalSubmitBtn) {
        finalSubmitBtn.addEventListener('click', async function (e) {
            e.preventDefault();
            await handleFinalSubmit();
        });
    }

    // Attach autosave listeners to all inputs
    document.querySelectorAll('#wizard-form input, #wizard-form select, #wizard-form textarea').forEach(input => {
        input.addEventListener('change', triggerAutosave);
        input.addEventListener('keyup', () => {
            clearTimeout(autosaveTimeout);
            autosaveTimeout = setTimeout(triggerAutosave, 1500);
        });
    });
}

function updateStepUI(step) {
    currentStep = step;

    // Show active step panel
    document.querySelectorAll('.wizard-step-panel').forEach(panel => {
        panel.classList.remove('active');
    });
    const activePanel = document.getElementById(`step-panel-${step}`);
    if (activePanel) {
        activePanel.classList.add('active');
    }

    // Update Progress Indicator
    document.querySelectorAll('.step-indicator-item').forEach(item => {
        const itemStep = parseInt(item.getAttribute('data-step'));
        item.classList.remove('active');
        if (itemStep === step) {
            item.classList.add('active');
        } else if (itemStep < step) {
            item.classList.add('completed');
        }
    });

    // Update Progress Bar Width
    const activeLine = document.querySelector('.wizard-progress-active-line');
    if (activeLine) {
        const percent = ((step - 1) / (totalSteps - 1)) * 100;
        activeLine.style.width = `calc(${percent}% - 20px)`;
    }

    // Scroll to top of wizard
    const wizardContainer = document.querySelector('.wizard-container');
    if (wizardContainer) {
        wizardContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // If step 8, populate review
    if (step === 8) {
        populateReviewSection();
    }
}

function goToStep(step) {
    if (step >= 1 && step <= totalSteps) {
        updateStepUI(step);
    }
}

async function handleStepSubmit(step) {
    const panel = document.getElementById(`step-panel-${step}`);
    if (!panel) return;

    // Validate current step fields
    const inputs = panel.querySelectorAll('input[required], select[required]');
    let isValid = true;
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
        }
    });

    // Password matching validation on Step 1
    if (step === 1) {
        const pwd = document.getElementById('field-password');
        const confirmPwd = document.getElementById('field-confirm-password');
        if (pwd && confirmPwd && pwd.value !== confirmPwd.value) {
            confirmPwd.classList.add('is-invalid');
            showToast('Passwords do not match / கடவுச்சொற்கள் பொருந்தவில்லை', 'danger');
            return;
        }
    }

    if (!isValid) {
        showToast('Please fill all required fields / தேவையான விவரங்களை நிரப்பவும்', 'warning');
        return;
    }

    // Prepare FormData
    const formData = new FormData();
    const panelInputs = panel.querySelectorAll('input, select, textarea');
    panelInputs.forEach(input => {
        if (input.type === 'file') {
            if (input.files.length > 0) {
                if (input.multiple) {
                    for (let i = 0; i < input.files.length; i++) {
                        formData.append(input.name, input.files[i]);
                    }
                } else {
                    formData.append(input.name, input.files[0]);
                }
            }
        } else if (input.type === 'checkbox') {
            if (input.checked) {
                formData.append(input.name, input.value || 'true');
            }
        } else if (input.type === 'radio') {
            if (input.checked) {
                formData.append(input.name, input.value);
            }
        } else {
            formData.append(input.name, input.value);
        }
    });

    const nextBtn = panel.querySelector('.btn-wizard-next');
    const originalText = nextBtn ? nextBtn.innerHTML : '';
    if (nextBtn) {
        nextBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Saving...';
        nextBtn.disabled = true;
    }

    try {
        const response = await fetch(`/api/register/step/${step}`, {
            method: 'POST',
            body: formData
        });

        const res = await response.json();
        if (response.ok && res.success) {
            goToStep(res.next_step);
            showToast(`Step ${step} saved successfully / விவரங்கள் சேமிக்கப்பட்டன`, 'success');
        } else {
            showToast(res.error || 'Validation failed', 'danger');
        }
    } catch (err) {
        console.error(err);
        showToast('Network error while saving step', 'danger');
    } finally {
        if (nextBtn) {
            nextBtn.innerHTML = originalText;
            nextBtn.disabled = false;
        }
    }
}

async function handleFinalSubmit() {
    const finalBtn = document.getElementById('btn-final-submit');
    const originalText = finalBtn ? finalBtn.innerHTML : '';
    if (finalBtn) {
        finalBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Submitting...';
        finalBtn.disabled = true;
    }

    const panel8 = document.getElementById('step-panel-8');
    const formData = new FormData();
    if (panel8) {
        const inputs = panel8.querySelectorAll('input, textarea');
        inputs.forEach(input => formData.append(input.name, input.value));
    }

    try {
        const response = await fetch('/api/register/step/8', {
            method: 'POST',
            body: formData
        });

        const res = await response.json();
        if (response.ok && res.success) {
            showToast(res.message || 'Profile submitted successfully!', 'success');
            setTimeout(() => {
                window.location.href = res.redirect_url || '/dashboard';
            }, 1200);
        } else {
            showToast(res.error || 'Submission failed', 'danger');
            if (finalBtn) {
                finalBtn.innerHTML = originalText;
                finalBtn.disabled = false;
            }
        }
    } catch (err) {
        console.error(err);
        showToast('Network error during submission', 'danger');
        if (finalBtn) {
            finalBtn.innerHTML = originalText;
            finalBtn.disabled = false;
        }
    }
}

function triggerAutosave() {
    const currentPanel = document.getElementById(`step-panel-${currentStep}`);
    if (!currentPanel) return;

    const data = {};
    currentPanel.querySelectorAll('input, select, textarea').forEach(input => {
        if (input.type !== 'file' && input.type !== 'password') {
            if (input.type === 'radio' || input.type === 'checkbox') {
                if (input.checked) data[input.name] = input.value;
            } else {
                data[input.name] = input.value;
            }
        }
    });

    fetch('/api/register/autosave', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ step: currentStep, form_data: data })
    }).then(res => res.json()).then(res => {
        const badge = document.getElementById('autosave-status-badge');
        if (badge) {
            badge.style.display = 'inline-flex';
            setTimeout(() => { badge.style.display = 'none'; }, 2000);
        }
    }).catch(err => console.log('Autosave skipped', err));
}

function setupIncomeCalculator() {
    const incomeInput = document.getElementById('field-annual-income');
    const categoryBadge = document.getElementById('calculated-category-badge');

    if (!incomeInput) return;

    incomeInput.addEventListener('input', function () {
        const val = parseFloat(this.value) || 0;
        let catEn = '₹1L+';
        let catTa = '₹1 லட்சம்+';

        if (val >= 10000000) { catEn = '₹1Cr+'; catTa = '₹1 கோடி+'; }
        else if (val >= 5000000) { catEn = '₹50L+'; catTa = '₹50 லட்சம்+'; }
        else if (val >= 2500000) { catEn = '₹25L+'; catTa = '₹25 லட்சம்+'; }
        else if (val >= 1500000) { catEn = '₹15L+'; catTa = '₹15 லட்சம்+'; }
        else if (val >= 1000000) { catEn = '₹10L+'; catTa = '₹10 லட்சம்+'; }
        else if (val >= 500000) { catEn = '₹5L+'; catTa = '₹5 லட்சம்+'; }
        else if (val >= 300000) { catEn = '₹3L+'; catTa = '₹3 லட்சம்+'; }

        if (categoryBadge) {
            categoryBadge.innerHTML = `<span class="badge bg-warning text-dark fs-6 px-3 py-2"><i class="bi bi-tag-fill me-1"></i> ${catEn} / ${catTa}</span>`;
        }
    });
}

function setupPhotoPreviews() {
    const photoInput = document.getElementById('field-profile-photo');
    const previewContainer = document.getElementById('profile-photo-preview');

    if (photoInput && previewContainer) {
        photoInput.addEventListener('change', function () {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewContainer.innerHTML = `<img src="${e.target.result}" class="img-thumbnail rounded-circle shadow-sm" style="width: 120px; height: 120px; object-fit: cover;">`;
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    }

    const jathagamInput = document.getElementById('field-jathagam-photo');
    const jathagamPreview = document.getElementById('jathagam-photo-preview');
    if (jathagamInput && jathagamPreview) {
        jathagamInput.addEventListener('change', function () {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    jathagamPreview.innerHTML = `<img src="${e.target.result}" class="img-thumbnail rounded shadow-sm" style="max-height: 150px;">`;
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    }
}

async function checkResumeData() {
    try {
        const response = await fetch('/api/register/resume');
        const res = await response.json();
        if (res.resumed && res.data) {
            populateFormWithSavedData(res.data);
            if (res.current_step && res.current_step > 1) {
                goToStep(res.current_step);
                const alertEl = document.getElementById('resume-alert-banner');
                if (alertEl) alertEl.style.display = 'block';
            }
        }
    } catch (err) {
        console.log('No resume data found');
    }
}

function populateFormWithSavedData(data) {
    for (const [key, value] of Object.entries(data)) {
        const input = document.querySelector(`[name="${key}"]`);
        if (input) {
            if (input.type === 'radio') {
                const radio = document.querySelector(`[name="${key}"][value="${value}"]`);
                if (radio) radio.checked = true;
            } else if (input.type === 'checkbox') {
                input.checked = Boolean(value);
            } else {
                input.value = value;
            }
        }
    }
}

function populateReviewSection() {
    // Collect all field values from steps 1-7 and populate review card
    const getVal = (name, fallback = '-') => {
        const el = document.querySelector(`[name="${name}"]`);
        if (!el) return fallback;
        if (el.type === 'radio') {
            const checked = document.querySelector(`[name="${name}"]:checked`);
            return checked ? checked.value : fallback;
        }
        return el.value || fallback;
    };

    const reviewMap = {
        'review-name': `${getVal('first_name')} ${getVal('last_name')}`,
        'review-profile-for': getVal('profile_created_for'),
        'review-type': getVal('profile_type'),
        'review-marital-status': getVal('marital_status'),
        'review-email': getVal('email'),
        'review-mobile': getVal('mobile'),
        'review-dob': getVal('date_of_birth'),
        'review-height': getVal('height'),
        'review-religion-community': `${getVal('religion')} - ${getVal('community')}`,
        'review-location': `${getVal('city')}, ${getVal('district')}, ${getVal('state')}`,
        'review-education': getVal('qualification'),
        'review-job': `${getVal('job')} (${getVal('working_place')})`,
        'review-income': `₹${getVal('income')}`,
        'review-family': `${getVal('family_type')} Family | Father: ${getVal('father_name')}`,
        'review-horoscope': `Rasi: ${getVal('rasi')} | Nakshatra: ${getVal('nakshatra')} | Dosham: ${getVal('dosham')}`
    };

    for (const [id, val] of Object.entries(reviewMap)) {
        const el = document.getElementById(id);
        if (el) el.textContent = val;
    }
}
