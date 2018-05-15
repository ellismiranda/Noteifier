import subprocess
import re


def is_process_active(process):
    return process in get_active_processes()


def get_active_processes():
    data = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()
    processes = [re.split('\d:\d\d\.\d\d', str(process)) for process in data]
    return [process[1][1:-3] for process in processes[1:]]


def get_active_applications():
    return [application for application in get_active_processes() if '/Applications' in application]


def parse_application_names(applications):
    return {app.split('/')[2][:-4] for app in applications}


def is_application_active(process):
    return process in parse_application_names(get_active_applications())


def monitor_new_process(app_name, noteifier):
    named_processes = [app for app in get_active_applications() if app_name in app]
    noteifier.monitored_applications[app_name] = named_processes
    print('Added {}.'.format(app_name))

