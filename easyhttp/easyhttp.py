#!/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import secrets

hostName = "147.135.209.249"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(bytes("<html><head><title>MAZIARZ.TECH</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(secrets.token_hex(8), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
