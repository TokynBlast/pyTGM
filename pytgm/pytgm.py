
# Started: 3/15/2024

import os

class b64:
  class table:
      table_ = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!@#$%^&*()_+-=[]{}\\|/,.<>~`;:'" '''
      
      @staticmethod
      def tableGen(self, chars, times):
          table = encryption.b64.table.table_
          self.table = random.seq.modify.shuffle(self.table, times)
          return table
          
      @staticmethod
      def tableSet(self, chars): 
          if type(chars) == str: self.table = chars
              
  @staticmethod
  def encode(self, text):
      bins = str()
      for c in text:
          bins += '{:0>8}'.format(str(bin(ord(c)))[2:])
      while len(bins) % 3:
          bins += '00000000'
      d = 1
      for i in range(6, len(bins) + int(len(bins) / 6), 7):
          bins = bins[:i] + ' ' + bins[i:]
      bins = bins.split(' ')
      if '' in bins:
          bins.remove('')
      base64 = str()
      for b in bins:
          if b == '000000':
              base64 += '='
          else:
              base64 += self.table_[int(b, 2)]
      return base64
  @staticmethod
  def decode(self, text):
      bins = str()
      for c in text:
          if c == '=':
              bins += '000000'
          else:
              bins += '{:0>6}'.format(str(bin(encryption.b64.table.table_.index(c)))[2:])
      for i in range(8, len(bins) + int(len(bins) / 8), 9):
          bins = bins[:i] + ' ' + bins[i:]
      bins = bins.split(' ')
      if '' in bins:
          bins.remove('')
      text = str()
      for b in bins:
          if not b == '00000000':
              text += chr(int(b, 2))
      return text


class file:
    @staticmethod
    def readLine(name, line=0):
        x = open(name, 'r')
        x.readlines()[line]
        return x
        
    @staticmethod
    def modLine(line_num, text):
        with open(name, 'r') as code:
            lines = code.readlines()
        
        if 0 <= line_num < len(lines):
            lines[line_num] = new_text + '\n'
        
        with open('code', 'w') as code:
            code.writelines(lines)

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
