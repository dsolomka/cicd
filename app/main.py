from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = ''
serverPort = 80

curent_status = 200

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global curent_status
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>v1.0.0</p>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")