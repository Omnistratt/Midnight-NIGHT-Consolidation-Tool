#!/usr/bin/env python3
"""
Simple web server to run the Midnight Consolidation Tool.
Double-click this file to start the tool!
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

PORT = 8000
API_BASE = "https://scavenger.prod.gd.midnighttge.io"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow API requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        # Handle proxy requests to Midnight API
        if self.path.startswith('/api/donate_to/'):
            try:
                # Extract the path after /api/donate_to/
                api_path = self.path.replace('/api/donate_to/', '')

                # Build the full API URL
                url = f"{API_BASE}/donate_to/{api_path}"

                # Read request body
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length) if content_length > 0 else b'{}'

                # Make request to Midnight API
                req = urllib.request.Request(url, data=post_data, method='POST')
                req.add_header('Content-Type', 'application/json')

                try:
                    with urllib.request.urlopen(req, timeout=30) as response:
                        response_data = response.read()

                        # Send success response
                        self.send_response(response.status)
                        self.send_header('Content-Type', 'application/json')
                        self.end_headers()
                        self.wfile.write(response_data)

                except urllib.error.HTTPError as e:
                    # Forward HTTP errors from API
                    error_data = e.read()
                    self.send_response(e.code)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(error_data)

            except Exception as e:
                # Handle any other errors
                error_response = json.dumps({
                    "status": "error",
                    "message": str(e)
                }).encode('utf-8')

                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(error_response)
        else:
            # Not an API request, return 404
            self.send_error(404)

    def log_message(self, format, *args):
        # Simplified logging - only show API requests
        if '/api/donate_to/' in format:
            print(f"API Request: {args[0]}")
        pass

def main():
    # Change to the script's directory
    os.chdir(Path(__file__).parent)

    # Find an available port
    port = PORT
    max_port = PORT + 100

    print("=" * 60)
    print("MIDNIGHT CONSOLIDATION TOOL")
    print("=" * 60)
    print(f"\nFinding available port...")

    while port < max_port:
        try:
            # Try to bind to the port
            with socketserver.TCPServer(("", port), MyHTTPRequestHandler) as httpd:
                httpd.allow_reuse_address = True

                print(f"Server started successfully on port {port}!")
                print(f"API proxy enabled (bypasses CORS restrictions)")
                print(f"\nOpening tool in your browser...")
                print(f"   URL: http://localhost:{port}")
                print(f"\nIf the browser doesn't open automatically, copy this URL:")
                print(f"   http://localhost:{port}")
                print(f"\nIMPORTANT: Keep this window open while using the tool!")
                print(f"\nTo stop the server: Close this window or press Ctrl+C")
                print("=" * 60)
                print(f"\nWaiting for requests...")
                print()

                # Try to open browser
                try:
                    webbrowser.open(f'http://localhost:{port}')
                except:
                    print(f"   Could not auto-open browser. Please open manually.")

                # Start serving
                httpd.serve_forever()

        except OSError as e:
            error_msg = str(e).lower()
            if "address already in use" in error_msg or "only one usage" in error_msg:
                print(f"   Port {port} is busy, trying {port + 1}...")
                port += 1
                continue
            else:
                print(f"\nError starting server: {e}")
                print(f"\nPlease try the following:")
                print(f"  1. Close any programs using port {port}")
                print(f"  2. Wait a few seconds and try again")
                print(f"  3. Restart your computer if the problem persists")
                input("\nPress Enter to exit...")
                sys.exit(1)
        break

    # If we got here, no port was available
    if port >= max_port:
        print(f"\nCould not find an available port between {PORT} and {max_port}")
        print(f"\nPlease close some programs and try again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nServer stopped. You can close this window now.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)
