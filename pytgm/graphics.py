import os

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
