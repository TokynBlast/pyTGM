def read_line(name, line=0):
    """
    Returns a single line of a file
    """
    x = open(name, 'r', encoding="utf-8")
    x.readlines()[line]
    return x

def mod_line(name, new_text, line_num=0, placeholder=""):
    """
    Modifies a line of a file.
    If the specified line doesn't exist, adds new lines until the line exists.
    
    Args:
        name (str): The file name to modify.
        new_text (str): The new text for the specified line.
        line_num (int): The zero-based index of the line to modify.
        placeholder (str): The default text for new lines (if the file needs to grow).
    """
    try:
        # Read the file lines, or start with an empty list if the file doesn't exist
        try:
            with open(name, 'r', encoding="utf-8") as code:
                lines = code.readlines()
        except FileNotFoundError:
            lines = []

        # Extend the lines to include the specified line number, filling with placeholders
        while len(lines) <= line_num:
            lines.append(placeholder + '\n')

        # Modify the specified line
        lines[line_num] = new_text + '\n'

        # Write the updated lines back to the file
        with open(name, 'w') as code:
            code.writelines(lines)

    except Exception as e:
        print(f"An error occurred: {e}") # pylint: disable=broad-exception-caught
