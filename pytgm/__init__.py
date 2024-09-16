__all__ = ['random','random.number','random.number.integer','random.number.binary','random.seq','random.seq.choose','random.seq.choose.choice','random.seq.choose.choices','random.seq.modify','random.seq.modify.shuffle','random.seq.modify.duplicate','random.seq.modify.remove','file','file.read','file.read.document','file.read.line','file.read.char','file.modify','file.modify.section','terminal','terminal.animate','terminal.clear','terminal.color','terminal.getch']
__url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/'
__homepage__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/docs'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/source'
__changelog_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/change'

# Started: 3/15/2024


class random:
    class num:
        @staticmethod
        def integer(min_value, max_value):
            seed = 0

            with open('/dev/urandom', 'rb') as f:
                seed_bytes = f.read(4)

                for byte in seed_bytes:
                    seed = (seed << 8) + byte

            random_seed = (seed % (max_value - min_value + 1)) + min_value

            return random_seed
            
        def binary(): return random.number.integer(0,1)

    class seq:
        class choose:
            @staticmethod
            def choice(lst=None):
                if lst is None:
                    lst = []
                return lst[random.number.integer(0, len(lst) - 1)]

            def choices(lst, amnt): return [random.seq.choose.choice(lst) for _ in range(amnt)]

        class modify:
            @staticmethod
            def shuffle(lst, times=1):
                shuffled_list = lst[:]
                for i in range(times):
                    for i in range(len(shuffled_list)):
                        rand_index = random.number.integer(0, len(shuffled_list) - 1)
                        shuffled_list[i], shuffled_list[rand_index] = shuffled_list[rand_index], shuffled_list[i]
                return shuffled_list
            @staticmethod
            def duplicate(lst, times=1):
                shuffled_list = lst
                for i in range(times):
                    for i in range(len(shuffled_list)):
                        shuffled_list[i], shuffled_list[random.number.integer(0, len(shuffled_list) - 1)] = shuffled_list[random.number.integer(0, len(shuffled_list) - 1)], shuffled_list[i]
                return shuffled_list
            @staticmethod
            def remove(lst, amnt): return [lst.remove(random.seq.choose.choice(lst)) for _ in range(amnt)]
 
class encryption:
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

    class sha256:
        def encode():
            None

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
        def char(name, character_num=0): char = open(name, 'r').read(character_num); return char

    class modify:
        def section(from_, to_):
            pass

class graphics:
    @staticmethod
    def animate(frames, times, wait, clr=True):
        if type(frames) not in (tuple, list, dict): pass
        from time import sleep
        for frame in range(times):
            print(frames[frame])
            sleep(wait)
            if clr: terminal.clear()
                
    def clear():print('\033[H\033[J', end='')

    def color(r,g,b):
        print(f"\033[38;2;{r};{g};{b}m")
            
    def col_reset():
        print("\033[0m")

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
