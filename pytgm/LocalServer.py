import socket
import threading

def server(host='localhost', PORT_='5000'):
    def server_(host,PORT_):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT_))
        server_socket.listen()
        
        clients = []
        
        def handle_client(client):
            while True:
                try:
                    message = client.recv(1024)
                    for client in clients:
                        client.send(message)
                except:
                    clients.remove(client)
                    client.close()
                    break
    
        def receive():
            while True:
                client, address = server_socket.accept()
                print(f"Connected with {address}")
                clients.append(client)
                client.send('Connected to the server!'.encode('ascii'))
                thread = threading.Thread(target=handle_client, args=(client,))
                thread.start()
        
        print("Server is waiting for connections...")
        receive()
    
    server_thread = threading.Thread(target=server_)
    server_thread.start()

def client(To_send, host, PORT_):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, PORT_))
    
    def receive():
        messages = []
        while True:
            try:
                message = client_socket.recv(1024).decode('ascii')
                messages.append(message)
            except:
                print("An error occurred!\nDisconnecting from the server.")
                client_socket.close()
                break
        return messages
    
    def write():
        while True:
            message = To_send
            if message:
                client_socket.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    
    write_thread = threading.Thread(target=write)
    write_thread.start()
