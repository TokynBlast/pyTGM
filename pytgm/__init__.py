__all__ = ['random','random.num','random.num.integer','random.num.binary','random.choose','random.seq','random.seq.modify','random.seq.modify.shuffle','random.seq.modify.duplicate','random.seq.modify.remove','file','file.readLine','file.modLine','graphics','graphics.cls','graphics.color','graphics.res','graphics.markup.bold','graphics.markup.italic','graphics.markup.underline','getch','sound','sound.file','sound.frequency','sound.frequency_big','Board','Board.boards','Board.add','Board.remove','Board.modify','LocalServer','b64','b64.table.table_','b64.table.tableGen','b64.table.tableSet','b64.encode','b64.decode']
__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

import .random as random
import .b64 as b64
import .file as file
import .board as board
import .sound as sound
import .graphics as graphics


def LocalServer(PORT_, To_send):
    import socket
    import threading
    import time

    def server(PORT_):
        HOST = ''
        PORT=PORT_
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        
        clients = []
        
        def broadcast(message):
            for client in clients:
                client.send(message)
        
        def handle_client(client):
            while True:
                try:
                    message = client.recv(1024)
                    broadcast(message)
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

    def client():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 5000))
        
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

    server_thread = threading.Thread(target=server)
    server_thread.start()
    
    time.sleep(1)

    client()
