# client.py

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 12345

# Connect to the server
client_socket.connect((host, port))

while True:
    # Input a message to send to the server
    message = input("Enter a message to send to the server: ")
    client_socket.send(message.encode())

    if message.lower() == 'close':
        break  # Break the loop if the user types 'close'

    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

print("Closing connection with the server.")
client_socket.close()
