from handlers.processes import parse_application_names, get_active_applications
from handlers.tools import check_files, generate_open_files_command, notify_notes, load_monitored, store_monitored
import threading
import time


class NoteifierThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.monitored_applications = load_monitored()
        self.accounted_for = {app for app in parse_application_names(get_active_applications()) if app in self.monitored_applications}
        self.paused = threading.Event()
        self.paused.clear()

    def run(self):
        while not self.paused.is_set():
            applications_open = get_active_applications()
            open_application_names = parse_application_names(applications_open)
            for application in self.monitored_applications:
                if application in open_application_names and application not in self.accounted_for:
                    files = check_files(application)
                    if files:
                        cmd = generate_open_files_command(files)
                        time.sleep(2)
                        notify_notes(application, cmd)
                    self.accounted_for.add(application)
            self.clean_accounted_for()
            time.sleep(3)

    def pause(self):
        self.paused.set()

    def resume(self):
        self.paused.clear()

    def clean_accounted_for(self):
        self.accounted_for = {app for app in self.accounted_for if app in parse_application_names(get_active_applications())}

    def quit(self):
        self.pause()
        store_monitored(self.monitored_applications)
