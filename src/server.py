"""
Local Dashboard Server Module.
Launches an instant HTTP server to view the interactive web dashboard on localhost.
"""

import http.server
import socketserver
import webbrowser
from pathlib import Path


PORT = 8000


def run_dashboard_server(dashboard_dir: str = "web_dashboard", port: int = PORT):
    web_dir = Path(dashboard_dir).resolve()
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(web_dir), **kwargs)

    print("=" * 65)
    print("NETFLIX DATA SCIENCE BUSINESS INSIGHTS DASHBOARD SERVER")
    print("=" * 65)
    print(f"[INFO] Serving dashboard from: {web_dir}")
    print(f"[INFO] Open in your browser: http://localhost:{port}")
    print("[INFO] Press CTRL+C to terminate the server.\n")

    # Attempt to open browser automatically
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass

    with socketserver.TCPServer(("", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[INFO] Dashboard server stopped gracefully.")


if __name__ == "__main__":
    run_dashboard_server()
