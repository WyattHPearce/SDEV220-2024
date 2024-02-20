"""
    Author:  Wyatt H. Pearce
    Date: 2/19/2024
    Section: 15.1
    Description:
    This program creates separate processes, each waiting random amounts of time, then printing the current time.
"""
# Import what I need based on instructions
import multiprocessing
from random import randint
from time import sleep
from datetime import datetime

# Process functions
def print_current_time(process_name) -> None:
    sleep_time: int = randint(1, 4)  # Random sleep time between 1 and 4 seconds
    sleep(sleep_time)
    # use datetime.datetime.now().isoformat() to print current time
    current_time = datetime.now().isoformat()
    print(f"Process {process_name}: Current Time - {current_time}")


if __name__ == '__main__':
    # processes
    process1: multiprocessing.Process = multiprocessing.Process(target=print_current_time, args=("1",))
    process2: multiprocessing.Process = multiprocessing.Process(target=print_current_time, args=("2",))
    process3: multiprocessing.Process = multiprocessing.Process(target=print_current_time, args=("3",))

    # start processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for all processes to finish
    process1.join()
    process2.join()
    process3.join()

    print("All processes have finished")
# exit