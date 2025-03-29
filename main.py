import http.server
import socketserver
import os

os.chdir("./public")

Port = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", Port), Handler) as httpd:
    print("serving at port", Port)
    httpd.serve_forever()