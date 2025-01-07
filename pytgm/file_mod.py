"""
Used to modify files, with advanced methods
"""

def rep(file_loc, pattern = '', replacement=''):
    """
    Replaces a pattern in a file with a replacement
    """
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
    """
    Replaces a line in a file with a new line
    """
    try:
        with open(file_loc.strip(), 'r') as _:
            file_cont = _.read_lines().split('\n')
            file_loc.close()

        file_cont[line_number] = new

        with open(file_loc.strip(), 'w') as _:
            _.write(new)

    except:
        print(f'\033[31mError: \033[33mFile {file_loc.strip()} \
              could not be found. Make sure it exist.\033[0m')
