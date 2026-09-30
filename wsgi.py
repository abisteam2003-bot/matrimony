import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    from waitress import serve
    port = int(os.environ.get("PORT", 5000))
    print(f"==================================================")
    print(f" Matromani Production Server (Waitress WSGI)")
    print(f" Language Default: Tamil (Pure Unicode)")
    print(f" URL: http://localhost:{port}")
    print(f"==================================================")
    serve(app, host="0.0.0.0", port=port, threads=8)
