"""
LocalServer

This module facilitates local server-client communication
using sockets and threading.
"""

import socket
import threading

@staticmethod
def server(host: str = 'localhost', port: int = 5000) -> None:
    """
    Starts a multithreaded server to handle client connections.
    """
    def server_():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen()

        clients = []

        def handle_client(client_socket):
            """
            Handles communication with a single client.
            """
            while True:
                try:
                    message = client_socket.recv(1024)
                    for conn in clients:
                        conn.send(message)
                except Exception as e: # pylint: disable=broad-exception-caught
                    print(f"Error with client: {e}")
                    clients.remove(client_socket)
                    client_socket.close()
                    break

        def receive():
            """
            Accepts incoming client connections.
            """
            while True:
                client_socket, address = server_socket.accept()
                print(f"Connected with {address}")
                clients.append(client_socket)
                client_socket.send('Connected to the server!'.encode('ascii'))
                thread = threading.Thread(target=handle_client, args=(client_socket,))
                thread.start()

        print("Server is waiting for connections...")
        receive()

    server_thread = threading.Thread(target=server_)
    server_thread.start()

@staticmethod
def client(message: str, host: str, port: int) -> None:
    """
    Connects to a server and sends a message.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    def receive():
        """
        Receives messages from the server.
        """
        messages = []
        while True:
            try:
                received_message = client_socket.recv(1024).decode('ascii')
                messages.append(received_message)
            except Exception as e: # pylint: disable=broad-exception-caught
                print(f"Error receiving message: {e}")
                client_socket.close()
                break
        return messages

    def write():
        """
        Sends a message to the server.
        """
        while True:
            if message:
                client_socket.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
