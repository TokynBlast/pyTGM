__all__ = ['random','random.num','random.num.integer','random.num.binary','random.choose','random.seq','random.seq.modify','random.seq.modify.shuffle','random.seq.modify.duplicate','random.seq.modify.remove','file','file.readLine','file.modLine','graphics','graphics.cls','graphics.color','graphics.res','graphics.markup.bold','graphics.markup.italic','graphics.markup.underline','getch','sound','sound.file','sound.frequency','Board','Board.boards','Board.add','Board.remove','Board.modify','LocalServer','b64','b64.table.table_','b64.table.tableGen','b64.table.tableSet','b64.encode','b64.decode']
__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

# Started: 3/15/2024

import os

class random:
    class num:
        @staticmethod
        def integer(min_value, max_value, seed=None):
            if seed == None:
                try: time()
                except: from time import time
                seed = int(time() * 1000)

            number = (seed % (max_value - min_value + 1)) + min_value

            return number

        def binary():
            return random.num.integer(0,1)


    class seq:
        def choose(lst, amnt=1):
          return [random.seq.choose.choice(lst) for _ in range(amnt)]

        class modify:
            @staticmethod
            def shuffle(lst, times=1):
                shuffled_list = lst[:]
                for i in range(times):
                    for i in range(len(shuffled_list)):
                        rand_index = random.num.integer(0, len(shuffled_list) - 1)
                        shuffled_list[i], shuffled_list[rand_index] = shuffled_list[rand_index], shuffled_list[i]
                return shuffled_list
                
            @staticmethod
            def duplicate(lst, times=1):
                shuffled_list = lst
                for i in range(times):
                    for i in range(len(shuffled_list)):
                        shuffled_list[i], shuffled_list[random.num.integer(0, len(shuffled_list) - 1)] = shuffled_list[random.num.integer(0, len(shuffled_list) - 1)], shuffled_list[i]
                return shuffled_list
                
            @staticmethod
            def remove(lst, amnt): return [lst.remove(random.seq.choose.choice(lst)) for _ in range(amnt)]
 
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
            
    def modLine(line_num, text):
        with open(name, 'r') as code:
            lines = code.readlines()
        
        if 0 <= line_num < len(lines):
            lines[line_num] = new_text + '\n'
        
        with open('code', 'w') as code:
            code.writelines(lines)


class graphics:
    def cls():
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        else:
            print('\033[H\033[J', end='')

    def color(r,g,b): return f"\x1b[38;2;{r};{g};{b}m"
                
    res = "\x1b[0m"

    class markup:
        bold = '\x1b[1m'
        italic = '\x1b[3m'
        underline = '\x1b[4m'

class sound:
    def file(path):
        try:
            from winsound import PlaySound as PS, SND_FILENAME
            PS(path, SND_FILENAME)
        
        except:
            #macOS

            if os.uname().sysname == 'Darwin':
                system(f'afplay {path}')
             
            try: uname()
            except: from os import uname
            if uname().sysname == 'Darwin':
                try: system('echo  ')
                except: import system
                os.system(f'afplay {path}')
                
            #Linux
            else:
                try: system('echo  ')
                except: from os import system
                system(f'aplay {path}')

    
    
    
    def frequency(frequency, duration, sample_rate=44100, volume=0.5):
        import wave, math, os, array
        n_samples = int(sample_rate * duration)

        samples = array.array('h')
        
        for i in range(n_samples):
            t = i / sample_rate
            sample_value = volume * math.sin(2 * math.pi * frequency * t)
            samples.append(int(sample_value * 32767))

        with wave.open('temp_tone.wav', 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(samples.tobytes())

        if os.name == 'nt':
            os.system('start temp_tone.wav')
        elif os.name == 'posix':
            os.system('afplay temp_tone.wav' if os.uname().sysname == 'Darwin' else 'aplay temp_tone.wav')

    ''' Which one works better?
    
    def frequency(frequency, duration, sample_rate=44100, volume=0.5):
        import wave
        import math

        n_samples = int(sample_rate * duration)
        samples = []
        for i in range(n_samples):
            sample = volume * math.sin(2 * math.pi * frequency * (i / sample_rate))
            samples.append(int(sample * 32767))  # Convert to 16-bit PCM format

        # Write to a temporary WAV file
        with wave.open('temp_tone.wav', 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(bytearray(samples))

        if os.name == 'nt':  # For Windows
            os.system('start temp_tone.wav')
        elif os.name == 'posix':  # For macOS and Linux
            os.system('afplay temp_tone.wav' if os.uname().sysname == 'Darwin' else 'aplay temp_tone.wav')
    '''



def getch(times=1):
    try:
        from msvcrt import getch as g
        for i in range(times):
            if g == 'b\xe0': return 'ArrowDown'
            else: return g()

    except:
        from sys import stdin
        from tty import setraw
        from termios import tcsetattr, TCSADRAIN, tcgetattr
        for i in range(times):
            fd = stdin.fileno()
            old = tcgetattr(fd)
            try:
                setraw(fd)
                c = stdin.read(1)
                if c == '\x1b':
                    c = stdin.read(2)
                    if c == '[A': return 'ArrowUp'
                    elif c == '[B': return 'ArrowDown'
                    elif c == '[C': return 'ArrowRight'
                    elif c == '[D': return 'ArrowLeft'
                    else: return c
                else:
                    if c == ' ': return 'space'
                    else: return c
            finally: tcsetattr(fd, TCSADRAIN, old)

class Board:
    boards = []

    @staticmethod
    def add(title, player=None, value=None):
        for board in Board.boards:
            if title in board:
                if player:
                    board[title][player] = value
                return
        Board.boards.append({title: {player: value}} if player else {title: {}})

    @staticmethod
    def remove(title, player=None):
        for board in Board.boards:
            if title in board:
                if player:
                    if player in board[title]:
                        del board[title][player]
                        if not board[title]:
                            Board.boards.remove(board)
                    return
                else:
                    Board.boards.remove(board)
                    return

    @staticmethod
    def modify(title, player, f_value):
        for board in Board.boards:
            if title in board and player in board[title]:
                board[title][player] = eval(f"{board[title][player]} {f_value}")

def LocalServer(PORT_):
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
                    print("An error occurred!")
                    client_socket.close()
                    break
            return messages
        
        def write():
            while True:
                message = input('')
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
