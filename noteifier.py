from models.constants import monitored_applications
from handlers.processes import get_active_processes
from handlers.tools import app_to_name, app_to_keyword, check_files, generate_open_files_command, notify
import threading
import time


class Noteifier():
    def __init__(self):
        self.accounted_for = [p for p in get_active_processes() if p in monitored_applications]
        self.paused = threading.Event()
        self.paused.clear()

    def run(self):
        while True:
            while not self.paused.is_set():
                applications_open = get_active_processes()
                for application in monitored_applications:
                    if application in applications_open and application not in self.accounted_for:
                        files = check_files(app_to_keyword(application))
                        if files:
                            cmd = generate_open_files_command(files)
                            time.sleep(2)
                            notify(message='Click on me to open notes about {}'.format(app_to_name(application)), title='Noteifier', command=cmd)
                            self.accounted_for.append(application)

    def pause(self):
        self.paused.set()

    def resume(self):
        self.paused.clear()
