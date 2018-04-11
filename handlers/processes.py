from models.constants import monitored_applications2
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


def monitor_new_process():
    print('Please make sure the desired application is running before attempting to add it.')
    new_app = input('Enter the name of the new application to monitor: ')
    while not is_application_active(new_app):
        print('Can\'t find {} running. Please double check the name and that the app is running.'.format(new_app))
        new_app = input('Enter the name of the new application to monitor: ')
    if new_app in monitored_applications2:
        print('Already monitoring {}.'.format(new_app))
    else:
        named_processes = [app for app in get_active_applications() if new_app in app]
        monitored_applications2[new_app] = named_processes
        print('Added {}.'.format(new_app))

