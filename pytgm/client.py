import socket
import time
import threading

def receive_messages(client_socket):
    while True:
        try:
            response = client_socket.recv(1024).decode('utf-8')
            if not response:
                break
            print(f"{response}")
        except Exception as e:
            print(f"Error receiving data: {str(e)}")
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = "127.0.0.1"
server_port = 8080 

client_socket.connect((server_host, server_port))

# Start a thread to continuously receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.daemon = True
receive_thread.start()

while True:
    message = input()
    
    if message.lower() == 'exit':
        break

    client_socket.send(message.encode('utf-8'))

client_socket.close()
