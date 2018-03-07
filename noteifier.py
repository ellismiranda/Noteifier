from models.constants import monitored_applications
from handlers.processes import lookup_process, get_active_processes
from handlers.tools import app_to_name, app_to_keyword, check_files, generate_open_files_command, notify
from twisted.internet import task, reactor
import threading
import time

accounted_for = [p for p in get_active_processes() if p in monitored_applications]


def noteifier():
    while True: # comment out for wrapper. ALSO REMOVE THIS AND MAKE A THREADABLE CLASS
        for application in monitored_applications:
            if lookup_process(application):
                if application not in accounted_for:
                    name = app_to_name(application)
                    files = check_files(app_to_keyword(application))
                    if files:
                        cmd = generate_open_files_command(files)
                        time.sleep(2)
                        notify(message='Click on me to open notes about {}'.format(name), title='Noteifier', command=cmd)
                        accounted_for.append(application)


def wrapper(fun):
    looper = task.LoopingCall(fun)
    looper.start(5)
    reactor.run()


class Noteifier():
    def __init__(self):
        self.paused = threading.Event().clear()

    def run(self):
        while True:
            if not self.paused.is_set():
                for application in monitored_applications:
                    if lookup_process(application):
                        if application not in accounted_for:
                            files = check_files(app_to_keyword(application))
                            if files:
                                cmd = generate_open_files_command(files)
                                time.sleep(2)
                                notify(message='Click on me to open notes about {}'.format(app_to_name(application)), title='Noteifier', command=cmd)
                                accounted_for.append(application)

    def pause(self):
        self.paused.set()

    def resume(self):
        self.paused.clear()
