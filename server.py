#!/usr/bin/python3.7

from socketserver import TCPServer, BaseRequestHandler
from time import sleep
import sys

class MyRequestHandler(BaseRequestHandler):

    def handle(self):
        self.request.send(
            b"HTTP/1.1 200 Ok\015\012"
            b"Content-Type: text/plain\015\012"
            b"Transfer-Encoding: chunked\015\012"
            b"Access-Control-Allow-Origin: *\015\012"
            b"\015\012"
        )
        sleep(2)
        self.request.send(
            b"3;param1=paramval1\015\012"
            b"foo\015\012"
        )
        sleep(2)
        self.request.send(
            b"12;param2=paramval2\015\012"
            b"quux is not a word\015\012"
        )
        sleep(2)
        self.request.send(
            b"0\015\012"
            b"\015\012"
        )
        self.request.send(
            b"X-Trailer-Header: Trailer-Header-Value\015\012"
        )

if __name__ == "__main__":
    server = TCPServer(("localhost", 8080), MyRequestHandler)
    server.handle_request()
    sys.exit(0)
