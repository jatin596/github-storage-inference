import http.server
import socketserver
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting minimal Python server")

PORT = 8080 # TODO:

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    logging.info(f"Serving on port {PORT}")
    httpd.serve_forever()
