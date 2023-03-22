"""
Manager script for the pool module.
Run this script to start the pool manager.
"""

if __name__ == "__main__":
    import argparse
    from .server import start_server
    #import http.server # im using http.server because it's easy to code but i may switch to socket later.
    #from threading import Thread
    
    parser = argparse.ArgumentParser(
        description="""
        Pool manager script.
        Run this script to start the pool manager.
        """
    )
    parser.add_argument("-p", "--port", type=int, default=2048, help="Port to run the server on.")
    parser.add_argument("-a", "--address", type=str, default="127.0.0.1", help="Address to run the server on.")
    parser.add_argument("-d", "--debug", action="store_true", help="Run the server in debug mode.")
    
    args = parser.parse_args()

    # start the server
    start_server(args.address, args.port, args.debug)
    #http.server.HTTPServer((args.address, args.port), http.server.BaseHTTPRequestHandler).serve_forever()
