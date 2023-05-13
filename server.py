#!/usr/bin/env python3

import http.server
import socketserver

# define the port to run the server on
PORT = 8000

# define the handler to use for incoming requests
handler = http.server.CGIHTTPRequestHandler

# set the current directory as the root of the web server
httpd = socketserver.TCPServer(("", PORT), handler)
httpd.allow_reuse_address = True

print(f"Serving CGI scripts on http://localhost:{PORT}")

# start the server and keep it running until interrupted
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
