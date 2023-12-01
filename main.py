# Advent of Code 2023
# Author: dmck

import os
from datetime import datetime

def run_advent_day(day):
    # get current directory
    current_dir = os.path.dirname(__file__)
    # get path to days / day / main.py
    path = os.path.join(current_dir, "days", str(day), "main.py")
    # if the path exists, call it:
    if os.path.exists(path):
        # run the day's main.py
        os.system(f"python {path}")


if __name__ == '__main__':
    # Get today's date
    today = datetime.now()

    # Check if today is between December 1 and December 25, 2023
    if 12 >= today.month >= 1 and 1 <= today.day <= 25 and today.year == 2023:
        # Run the corresponding Advent day script
        run_advent_day(today.day)
    else:
        print("Sorry, keep counting the days until Christmas!")
