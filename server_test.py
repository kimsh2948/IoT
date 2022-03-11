import http.server
import socketserver
import json

HOST = '192.168.0.6'
PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type'.encode(), 'text/html'.encode())
        self.end_headers()

        self.wfile.write(json.dumps({'success': True}).encode())

        content_length = int(self.headers['Content-Length'])
        json_string = self.rfile.read(content_length).decode("utf-8")
        
        data = json.loads(json_string)
        print(data)

httpd = socketserver.TCPServer((HOST, PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()