import time
import os
import io

string = io.StringIO


# - Exit Function
def exit_func():
    print("")
    print('Exiting...')
    time.sleep(1)
    os.system('clear')
    exit()
