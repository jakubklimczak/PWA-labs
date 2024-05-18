import http.server
import ssl

server_address = ('localhost', 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="localhost.pem",
                               keyfile="localhost-key.pem",
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()
