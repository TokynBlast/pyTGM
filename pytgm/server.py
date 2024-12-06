import socket
import threading

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to listen on
host = "127.0.0.1"  # Change this to your desired host
port = 8080  # Change this to your desired port

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {host}:{port}")

# List to store connected clients
connected_clients = []

def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"{client_socket.getpeername()}: {data}")

            # Send the received data to all connected clients
            for client in connected_clients:
                if client != client_socket:
                    try:
                        client.send(data.encode('utf-8'))
                    except Exception as e:
                        print(f"Error sending data to {client.getpeername()}: {str(e)}")

        except Exception as e:
            print(f"Error: {str(e)}")
            break

    # Remove the client from the list of connected clients
    connected_clients.remove(client_socket)
    client_socket.close()

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"A new client has joined.")

    # Add the client to the list of connected clients
    connected_clients.append(client_socket)

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
