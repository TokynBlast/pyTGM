__all__ = ['random','random.num','random.num.integer','random.num.binary','random.seq','random.seq.choose','random.seq.choose.choice','random.seq.choose.choices','random.seq.modify','random.seq.modify.shuffle','random.seq.modify.duplicate','random.seq.modify.remove','file','file.read','file.read.document','file.read.line','file.read.char','graphics','graphics.cls','graphics.color','graphics.color.RGB','graphics.color.res','graphics.markup.bold','graphics.markup.italic','graphics.markup.underline','getch','sound','sound.file','sound.frequency','Board','Board.add','Board.remove','Board.modify','aat']
__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://youtube.tokynblast.space/programmingpytgm/source'
__changelog_url__ = 'https://youtube.tokynblast.space/programming/pytgm/change'

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
        class choose:
            @staticmethod
            def choice(lst=None):
                if lst is None:
                    lst = []
                    
                return lst[random.num.integer(0, len(lst) - 1)]

            def choices(lst, amnt): return [random.seq.choose.choice(lst) for _ in range(amnt)]

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
    class read:
        @staticmethod
        def document(name): return open(name, 'r').read()
            
        @staticmethod
        def line(name, line=0):
            x = open(name, 'r')
            x.readlines()[line]
            return x
        
        @staticmethod
        def char(name, character_num=0):
            char = open(name, 'r').read(character_num)
            return char

class graphics:
    def cls():
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        else:
            print('\033[H\033[J', end='')

    class color:
        def RGB(r,g,b):
            return f"\x1b[38;2;{r};{g};{b}m"
                
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
        
        # Initialize an array to store sample values
        samples = array.array('h')  # 'h' stands for 16-bit signed integers
        
        for i in range(n_samples):
            t = i / sample_rate  # Time value for the current sample
            sample_value = volume * math.sin(2 * math.pi * frequency * t)
            # Convert sample to 16-bit PCM format
            samples.append(int(sample_value * 32767))
        
        # Write to a temporary WAV file
        with wave.open('temp_tone.wav', 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 2 bytes for 16-bit audio
            wf.setframerate(sample_rate)
            wf.writeframes(samples.tobytes())
        
        # Play the file depending on the OS
        if os.name == 'nt':  # For Windows
            os.system('start temp_tone.wav')
        elif os.name == 'posix':  # For macOS and Linux
            os.system('afplay temp_tone.wav' if os.uname().sysname == 'Darwin' else 'aplay temp_tone.wav')



def getch(times=1):
    try:
        from msvcrt import getch as g
        for i in range(times):
            return g()

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
        # Add a new board or a new value to an existing board
        for board in Board.boards:
            if title in board:
                if player:
                    board[title][player] = value
                return
        Board.boards.append({title: {player: value}} if player else {title: {}})

    @staticmethod
    def remove(title, player=None):
        # Remove a value or a board
        for board in Board.boards:
            if title in board:
                if player:
                    if player in board[title]:
                        del board[title][player]
                        if not board[title]:  # If no players left, remove the board
                            Board.boards.remove(board)
                    return
                else:
                    Board.boards.remove(board)
                    return

    @staticmethod
    def modify(title, player, f_value):
        # Modify a value in an existing board
        for board in Board.boards:
            if title in board and player in board[title]:
                board[title][player] = eval(f"{board[title][player]} {f_value}")






def aat(text, font):
    def calculate_max_height(font):
        """Assume all characters have the same height."""
        for char in font.values():
            lines = char.split('\n')
            return len(lines)  # Return the height of the first character

    def pad_rows(char_rows, max_length):
        """Pad each row of the character to the right with minimal spaces and trim any trailing spaces."""
        return [row.rstrip().ljust(max_length) for row in char_rows]

    # Get the maximum height of any character (assumes all characters are the same height)
    max_height = calculate_max_height(font)

    # Split the input text into lines
    lines = text.split('\n')
    for line in lines:
        if not line.strip():  # If the line is empty, print a blank line and continue
            print('')
            continue

        # Initialize rows that will store the current line's output
        rows = ['' for _ in range(max_height)]
        for char in line:
            if char == ' ':  # Handle spaces separately
                max_length = len(rows[0])  # Use the length of the current row
                padded_char_rows = [' ' * max_length] * max_height
            elif char in font:
                # Get the character's representation and calculate its dimensions
                char_rows = font[char].split('\n')
                max_length = len(char_rows[0])  # Width of the first row (assumed constant)
                # Pad the character rows to the right and trim extra trailing spaces
                padded_char_rows = pad_rows(char_rows, max_length)
            else:
                # If character is not in font, create an empty space block with the same height
                max_length = len(rows[0])
                padded_char_rows = [' ' * max_length] * max_height

            # Add the padded character's rows to the current line's rows with no extra spacing
            for i in range(max_height):
                rows[i] += padded_char_rows[i]  # No extra spacing between characters

        # Print the final output for this line
        for row in rows:
            print(row.rstrip())  # Remove trailing spaces
        print()  # Add extra space between lines of text
