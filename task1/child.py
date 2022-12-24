#!/usr/bin/python3

import sys
from os import getpid, getppid, _exit
import time
import random

sleep_time = int(sys.argv[1])
print(f'Сhild[{getpid()}]: I am started. My PID {getpid()}. Parent PID {getppid()}.')
time.sleep(sleep_time)
print(f'Child[{getpid()}]: I am ended. PID {getpid()}. Parent PID {getppid()}.')
_exit(random.randint(0, 1))
