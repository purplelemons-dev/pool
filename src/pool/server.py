
import http.server

# TODO: add a file option to save the data to a file, defaults to no file.
# also add a way to load data from a file.

class Handler(http.server.BaseHTTPRequestHandler):

    @classmethod
    def set_root(cls,root:dict):
        cls.root = root

    def do_GET(self):
        # Path should be /table_name/(key/(subkey/...))
        path = self.path.split("/")[1:]
        table = path[0]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("Hello World!", "utf-8"))

def start_server(address, port, debug):
    import http.server
    Handler.set_root({})
    server = http.server.HTTPServer((address, port), Handler)
    print(f"Server started on {address}:{port}")
    server.serve_forever()
