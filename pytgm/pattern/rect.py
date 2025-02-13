""" Clears the terminal as it moves along """
import time as t
import sys

def rect(width, height, time=3, char=" "):
    """ Moves acress the terminal, and prints a space, to clear the screen """
    total_steps = (height * (height + 1)) // 2 + (height * (height - 1)) // 2 + (max(width - height, 0) * height) #pylint-ignore: line-too-long
    step_time = time / total_steps  # Calculate time per step

    # Left side
    for i in range(height):
        line_length = min(i + 1, width)
        for j in range(line_length):
            sys.stdout.write(f"\x1b[{j + 1};{i - j + 1}H{char}")
            sys.stdout.flush()
            t.sleep(step_time)

    # middle
    for i in range(height, width):
        for j in range(height):
            sys.stdout.write(f"\x1b[{j + 1};{i - j + 1}H{char}")
            sys.stdout.flush()
            t.sleep(step_time)

    # right side
    for i in range(height):
        for j in range(i, height):
            sys.stdout.write(f"\x1b[{j + 1};{width - (j - i)}H{char}")
            sys.stdout.flush()
            t.sleep(step_time)
