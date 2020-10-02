#!/usr/bin/python3.7

from socketserver import TCPServer, BaseRequestHandler
import sys

class MyRequestHandler(BaseRequestHandler):

    def handle(self):
        self.request.send(
            b"HTTP/1.1 200 Ok\015\012"
            b"Content-Type: text/plain\015\012"
            b"Transfer-Encoding: chunked\015\012"
            b"\015\012"
            b"3;param1=paramval1\015\012"
            b"foo\015\012"
            b"12;param2=paramval2\015\012"
            b"quux is not a word\015\012"
            b"0\015\012"
            b"\015\012"
            b"X-Trailer-Header: Trailer-Header-Value\015\012"
        )

if __name__ == "__main__":
    server = TCPServer(("localhost", 8080), MyRequestHandler)
    server.handle_request()
    sys.exit(0)
