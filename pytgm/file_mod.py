"""
Used to modify files, with advanced methods
"""

def rep(file_loc, pattern = '', replacement=''):
    try:
        with open(file_loc.strip(), 'r') as _:
            file_cont = _.read_lines().split('\n')
            file_loc.close()
        
        f_con_len = range(len(file_cont))
        for _ in f_con_len:
            file_cont[_].replace(pattern, replacement)
        
        with open(file_loc.strip(), 'w') as _:
            _.write(file_cont)
            _.close()
        
    except:
        print(f'\033[31mError: \033[33mFile {file_loc.strip()} could not be found. Make sure it exist.\033[0m')

def fm_line(file_loc, line_number = 0, new = ''):
    try:
        with open(file_loc.strip(), 'r') as _:
            file_cont = _.read_lines().split('\n')
            file_loc.close()

        file_cont[line_number] = new
        
        with open(file_loc.strip(), 'w') as _:
            _.write(new)
        
    except:
        print(f'\033[31mError: \033[33mFile {file_loc.strip()} could not be found. Make sure it exist.\033[0m')
    

def mod_line(file, txt, line, p_hold=''):
    fm_line(file, line, txt)
    del p_hold
    yellow = '\033[31m'
    red = '\033[33m'
    res = '\033[0m'
    print(f'{yellow}WARNING: {red}mod_line() will become fm_line in v4.2.0\nYou should begin using fm_line() as soon as possible.{res}')
