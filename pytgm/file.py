def read_line(name, line=0):
    """
    Returns a single line of a file
    """
    x = open(name, 'r')
    x.readlines()[line]
    return x

def mod_line(text, line=0):
    """
    Modifies a line of a file
    This will be able to do more than just a single line in the future
    Likely, multiple
    """
    with open(name, 'r') as code:
        lines = code.readlines()

    if 0 <= line_num < len(lines):
        lines[line_num] = new_text + '\n'

    with open('code', 'w') as code:
        code.writelines(lines)
    else: print("Invalid line space"
