import os
import subprocess
import re


def lookup_process(process):
    return process in get_active_processes()


def get_active_processes():
    data = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()
    processes = [re.split('\d:\d\d\.\d\d', str(process)) for process in data]
    return [process[1][1:-3] for process in processes[1:]]
