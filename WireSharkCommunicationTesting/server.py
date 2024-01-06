# server.py

import socket

# Create a socket object
#socket.AF_INET -> allows for ipv4 usage
#socket.SOCK_STREAM -> Uses TCP protocl
#Overall were creating a server socket which uses ipv4 for addressing and TCP for the protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Now wait for the client to connect
server_socket.listen(5)

print(f"Server listening on port number:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()

        if not data:
            break  # Break the loop if no data received

        print(f"Received from client: {data}")

        if data.lower() == 'close':
            break  # Break the loop if the client sends 'close'

        # Send a response back to the client
        response = input("Enter a message to send to the client: ")
        client_socket.send(response.encode())

    print("Closing connection with client.")
    client_socket.close()
    break  # Break the outer loop to close the server
