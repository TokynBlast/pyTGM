#for i in range(25):
#    print(f"\x1b[{25 - i};{i}H█", end="")

import time
import sys

# Number of lines
num_lines = 30

# Loop through the lines
for i in range(num_lines):
    for j in range(i + 1):
        # Move the cursor to the correct position
        print(f"\x1b[{j + 1};{i - j + 1}H█", end="")
        sys.stdout.flush()  # Ensure it gets printed immediately
        time.sleep(0.02)  # Slow down the effect for visibility
