# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import secrets

hostName = "localhost"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(bytes("<html><head><title>MAZIARZ.TECH</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>MAZIARZ.TECH</p>", "utf-8"))
        self.wfile.write(bytes("<p>losowy hex: ", "utf-8"))
        self.wfile.write(bytes(secrets.token_hex(4), "utf-8"))
        self.wfile.write(bytes("</p>", "utf-8"))
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