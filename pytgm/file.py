"""
Read or write to files, but a little bit more complex.
"""

def read_line(name, line=0):
    """
    Returns a single line of a file.

    Args:
        name (str): The file name to read from.
        line (int): The zero-based index of the line to read.
    
    Returns:
        str: The specified line from the file, or an empty string if the line does not exist.
    """
    try:
        with open(name, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            if line < len(lines):
                return lines[line].strip()
            return ""  # Return empty string if the line does not exist
    except FileNotFoundError:
        print(f"Error: File '{name}' not found.")
        return ""
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An unexpected error occurred: {e}")
        return ""

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
            with open(name, 'r', encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        # Extend the lines to include the specified line number, filling with placeholders
        while len(lines) <= line_num:
            lines.append(placeholder + '\n')

        # Modify the specified line
        lines[line_num] = new_text + '\n'

        # Write the updated lines back to the file
        with open(name, 'w', encoding='utf-8') as file:
            file.writelines(lines)

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An error occurred: {e}")
