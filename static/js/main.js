/**
 * Matromani Global JavaScript
 * Handles Shortlisting, Sending Interest, Dynamic Language Switch, and UI Feedback
 */

document.addEventListener('DOMContentLoaded', function () {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Handle Shortlist Button Clicks
    document.querySelectorAll('.btn-shortlist-toggle').forEach(btn => {
        btn.addEventListener('click', async function (e) {
            e.preventDefault();
            const profileId = this.getAttribute('data-profile-id');
            if (!profileId) return;

            const originalHtml = this.innerHTML;
            this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span>';

            try {
                const response = await fetch('/api/shortlist/toggle', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ profile_id: profileId })
                });

                const res = await response.json();
                if (response.status === 401 || res.login_required) {
                    showToast(res.error || 'Please login to shortlist / உள்நுழையவும்', 'warning');
                    setTimeout(() => {
                        window.location.href = '/login';
                    }, 1200);
                    return;
                }

                if (res.success) {
                    if (res.shortlisted) {
                        this.classList.remove('btn-outline-secondary');
                        this.classList.add('btn-danger');
                        this.innerHTML = '<i class="bi bi-heart-fill"></i> ' + (document.documentElement.lang === 'ta' ? 'சேர்க்கப்பட்டது' : 'Shortlisted');
                    } else {
                        this.classList.remove('btn-danger');
                        this.classList.add('btn-outline-secondary');
                        this.innerHTML = '<i class="bi bi-heart"></i> ' + (document.documentElement.lang === 'ta' ? 'விருப்பப்பட்டியல்' : 'Shortlist');
                    }
                    showToast(res.message, 'success');
                } else {
                    this.innerHTML = originalHtml;
                    showToast(res.error || 'Action failed', 'danger');
                }
            } catch (err) {
                console.error(err);
                this.innerHTML = originalHtml;
                showToast('Network error, please try again', 'danger');
            }
        });
    });

    // Handle Send Interest Button Clicks
    document.querySelectorAll('.btn-send-interest').forEach(btn => {
        btn.addEventListener('click', async function (e) {
            e.preventDefault();
            const profileId = this.getAttribute('data-profile-id');
            if (!profileId) return;

            const originalHtml = this.innerHTML;
            this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span>';

            try {
                const response = await fetch('/api/interest/send', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ profile_id: profileId })
                });

                const res = await response.json();
                if (response.status === 401 || res.login_required) {
                    showToast(res.error || 'Please login / உள்நுழையவும்', 'warning');
                    setTimeout(() => {
                        window.location.href = '/login';
                    }, 1200);
                    return;
                }

                if (res.success) {
                    this.classList.remove('btn-premium-primary');
                    this.classList.add('btn-secondary');
                    this.disabled = true;
                    this.innerHTML = '<i class="bi bi-check2-circle"></i> ' + (document.documentElement.lang === 'ta' ? 'விருப்பம் அனுப்பப்பட்டது' : 'Interest Sent');
                    showToast(res.message, 'success');
                } else {
                    this.innerHTML = originalHtml;
                    showToast(res.error || 'Action failed', 'danger');
                }
            } catch (err) {
                console.error(err);
                this.innerHTML = originalHtml;
                showToast('Network error, please try again', 'danger');
            }
        });
    });

    // Auto-dismiss Flash Alerts after 5 seconds
    setTimeout(() => {
        document.querySelectorAll('.alert-dismissible').forEach(alert => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
});

// Toast notification helper
function showToast(message, type = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'position-fixed bottom-0 end-0 p-3';
        container.style.zIndex = '1090';
        document.body.appendChild(container);
    }

    const toastEl = document.createElement('div');
    toastEl.className = `toast align-items-center text-white bg-${type} border-0 shadow-lg`;
    toastEl.setAttribute('role', 'alert');
    toastEl.setAttribute('aria-live', 'assertive');
    toastEl.setAttribute('aria-atomic', 'true');
    toastEl.innerHTML = `
        <div class="d-flex">
            <div class="toast-body fw-bold">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;

    container.appendChild(toastEl);
    const toast = new bootstrap.Toast(toastEl, { delay: 3500 });
    toast.show();

    toastEl.addEventListener('hidden.bs.toast', () => {
        toastEl.remove();
    });
}
