__all__ = ['encode', 'decode', 'clear', 'readFile', 'readChar', 'readLine', 'getch', 'animate', 'randint', 'choice', 'choices']
__url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/'
__homepage__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/docs'
__bug_tracker_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/bugs'
__source_code_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/source'
__changelog_url__ = 'https://youtube.tokynblast.space/programming/libraries/pytgm/change'


'''
Needs: Map Sizing
       Built-in x and y
       List for getch with multiple times key pressed
       threading
       sockets
       mid function stopping
       Table has no set table
       window data transfer
       time
       scenes

Need Finished: terminal/color
               sound/...
               score/board/...
               file/modify/...
               terminal/animate/from, to

FIX __all__
Make https://youtube.tokynblast.space/programming/libraries/pytgm the URL!!

'''
# Started: 3/15/2024


class random:
    class number:
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

class decode:
    def b64():
        None
    def sha56():
        None

class encode:
    def b64():
        None
    def sha56():
        None
 
class b64:
    @staticmethod
    def __init__(self, table):
        self.table = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!@#$%^&*()_+-=[]{}\\|/,.<>~`;:'" '''
    
    '''class table:
      @staticmethod
      def tableGen(chars, times=1, ):
          try: b64.__init__.table = shuffle(self.table, times)
          except: self.table = random.modify.shuffle(self.table, randint(times[0],times[1]))
          return self.table()
  
      def tableSet(chars): 
          if type(chars) == str: self.table = chars
          else: raise NonStrB64TableError(self)
    '''

    @staticmethod
    def encode(text):
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
                base64 += self.table[int(b, 2)]
        return base64
        
    @staticmethod
    def decode(text):
        bins = str()
        for c in text:
            if c == '=':
                bins += '000000'
            else:
                bins += '{:0>6}'.format(str(bin(self.table.index(c)))[2:])
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
        def char(name, character_num=0): char = open(name, 'r').read(character_num); return char

    class modify:
        def section(from_, to_):
            pass
'''
class score:
    class value:
        values = {}
        @staticmethod
        def newValue(name, value): values[name] = value
        @staticmethod
        def modifyValue(name, func, value): exec(self.values[name] {func} value')

    class board:
      # named board:
      # self.board = [{title:({title:value}, {title:value})}]
      # valued board:
      # self.board = [{title:(value, value, value)}}]
        self.valuedBoards = []
        self.namedBoards = []
'''        

class terminal:
    # Add from frame and to frame
    @staticmethod
    def animate(frames, times, wait, clr=True):
        if type(frames) not in (tuple, list, dict): pass
        from time import sleep
        for frame in range(times):
            print(frames[frame])
            sleep(wait)
            if clr: terminal.clear()
                
    def clear():print('\033[H\033[J', end='')

    def color():
        None


# Remove?
def prntChars(amnt, end_='\n'): [print('', end=end_) for _ in range(amnt)]



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


'''
Finish 'Modify'
Implement SHA 56 for encoding?
or something similar?

y: middle, bottom, top
x: left, center, right
Screen Placement (left, right, center, middle,  boottom, top [EX: x.y])

Path Tracking
  chance for direction (default: 12.5% to all 8)
  Range of sight
  Collision
  

Collision Detection
  character or coordinates?
  
  Errors:
    // UnknownMovementError
    // GrayMovementError - When an entity tries to move in a gray area (an area where movement possibilities are unknown)

Errors:
  UnknownEntityError - When an entity is called but not found ('Make sure the name is correct')
  Invalid
'''

'''






pyTMG/
├── random/
│   ├── number/
│   │   ├── integer
│   │   └── binary
│   └── seq/
│       ├── choose/
│       │   ├── choice
│       │   └── choices
│       └── modify/
│           ├── shuffle
│           ├── duplicate
│           └── remove
├── b64/
│   ├── encode
│   └── decode
├── files/
│   ├── read/
│   │   ├── file
│   │   ├── line
│   │   └── char
│   └── modify/
│       └── section
├── score/
│   ├── value/
│   │   ├── new
│   │   └── modify
│   └── board/
│       ├── named/
│       │   ├── modify
│       │   └── new
│       └── valued/
│           ├── modify
│           └── new
├├── terminal/
│   ├── animate
│   ├── clear
│   └── color
└── getch

Change encoding and decoding to this:
└── data/
    ├── encode
    └── decode

Write some code that puts it into b64, then into sha56, and when decoding, if the b64 -> sha56 doesnt match:
print("""You will have to reset, the save file is either corrupted, or has been modified.
Do you want to attempt a recovery or reset the save?""")

Input Handling:
input/
    keyboard/
        get_key
        get_keys
        get_keypress
    mouse/
        get_click
        get_position
This module would handle user input, both from the keyboard and mouse, providing functions to get key presses, key combinations, mouse clicks, and mouse cursor position.
Graphics and Rendering:
graphics/
    draw/
        print_text
        draw_shape
        draw_image
    color/
        set_color
        get_color
    screen/
        clear_screen
        resize_screen
This module would handle the rendering of text, shapes, and images, as well as color management and screen manipulation.
Sound and Audio:
audio/
    play_sound
    play_music
    set_volume
    pause
    resume
This module would provide functionality for playing sound effects and background music, as well as controlling the volume and playback.
Game State Management:
game/
    state/
        set_state
        get_state
        reset_state
    scene/
        change_scene
        get_current_scene
This module would handle the overall game state, allowing you to manage different scenes or levels, and provide functions to set, retrieve, and reset the game state.
UI and Widgets:
ui/
    widgets/
        Button
        Label
        TextBox
        ProgressBar
    layout/
        HorizontalLayout
        VerticalLayout
        GridLayout
This module would provide a set of common UI widgets and layout managers to help you create and arrange user interface elements in your terminal-based games.
Networking and Multiplayer:
network/
    server/
        start
        stop
        send
    client/
        connect
        disconnect
        send
This module would enable you to add networking capabilities to your games, allowing for multiplayer functionality and client-server communication.
Documentation and Utilities:
docs/
    tutorials
    examples
    api_reference
utils/
    timer
    event_manager
    config_loader
This section would include comprehensive documentation, example projects, and API reference, as well as utility functions to help with common game development tasks.
'''
