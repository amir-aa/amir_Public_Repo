import socket,requests
import select,base64,json
connections={}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('', 123)
server_socket.bind(server_address)

server_socket.listen(5)
server_socket.setblocking(False)

inputs = {server_socket: server_socket}
outputs = {}

while inputs:
    # Use select to wait for events on sockets
    readable, writable, exceptional = select.select(inputs.keys(), outputs.keys(), inputs.keys())

    # Handle readable sockets (new connections or incoming data)
    for sock in readable:
        if sock is server_socket:
            # Accept new connections
            client_socket, client_address = sock.accept()
            print("Connection from:", client_address)
            client_socket.setblocking(False)
            inputs[client_socket] = client_socket
        else:
        
            data = sock.recv(1024)
            if data:
               
                print("Received:", data.decode())
                
                # Echo back to the client
                outputs[sock] = data
            else:
                # Client closed the connection
                print("Client disconnected:", sock.getpeername())
                if sock in outputs:
                    del outputs[sock]
                del inputs[sock]
                sock.close()

    # Handle writable sockets (send outgoing data)
    for sock in writable:
        data = outputs.pop(sock)
        sock.sendall(data)

    # Handle exception
    for sock in exceptional:
        print("Exceptional condition on:", sock.getpeername())
        del inputs[sock]
        if sock in outputs:
            del outputs[sock]
        sock.close()
