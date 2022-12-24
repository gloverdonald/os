#!/usr/bin/python3

from os import fork, getpid, wait, execl, waitstatus_to_exitcode
import sys
import random


def new_children():
    child = fork()
    if child == 0:
        argument = str(random.randint(5, 10))
        execl("./child.py", "child", argument)
    print(f"Parent [{getpid()}]: I ran children process with PID {child}")


children_count = int(sys.argv[1])

for i in range(0, children_count):
    new_children()

while children_count > 0:
    child_pid, child_status = wait()
    child_status = waitstatus_to_exitcode(child_status)
    print(f"Parent[{getpid()}]: Child with PID {child_pid} terminated. Exit Status {child_status}.")
    if child_status == 0:
        children_count -= 1
    else:
        new_children()
