from models.constants import monitored_applications
from handlers.processes import parse_application_names, get_active_applications
from handlers.tools import check_files, generate_open_files_command, notify
import threading
import time


class Noteifier():
    def __init__(self):
        self.accounted_for = {app for app in parse_application_names(get_active_applications()) if app in monitored_applications}
        self.paused = threading.Event()
        self.paused.clear()

    def run(self):
        while not self.paused.is_set():
            applications_open = get_active_applications()
            open_application_names = parse_application_names(applications_open)
            for application in monitored_applications:
                if application in open_application_names and application not in self.accounted_for:
                    files = check_files(application)
                    if files:
                        cmd = generate_open_files_command(files)
                        time.sleep(2)
                        notify(message='Click on me to open notes about {}'.format(application), title='Noteifier', command=cmd)
                    self.accounted_for.add(application)
            self.clean_accounted_for()

    def pause(self):
        self.paused.set()

    def resume(self):
        self.paused.clear()

    def clean_accounted_for(self):
        self.accounted_for = {app for app in self.accounted_for if app in parse_application_names(get_active_applications())}
