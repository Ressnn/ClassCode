import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'UTF-8')
        cur_thread = threading.current_thread()
        if data == "ABC":
            print(self.request,": Passed")
            response = bytes("Passed","UTF-8")
        else:
            response = bytes("Failed","UTF-8")
            print("Recived:", data, " Which will not pass")
        
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass



# Port 0 means to select an arbitrary unused port
HOST, PORT = "localhost", 8889
server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
with server:
    ip, port = server.server_address
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    while True:
        pass
    server.shutdown()
    

