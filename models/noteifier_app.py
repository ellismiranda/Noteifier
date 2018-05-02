from noteifier import Noteifier
from threading import Thread
from handlers import tools
from models.constants import app_menu, monitored_applications
import rumps
import os


class NoteifierApp(rumps.App):
    def __init__(self):
        super(NoteifierApp, self).__init__("Noteifier")
        self.currdir = str(os.getcwd())
        self.icon = 'assets/icon.png'
        self.menu = app_menu
        self.noteifier = Noteifier()
        self.monitor = Thread(target=self.noteifier.run,)
        self.monitor.start()

    @rumps.clicked('Status: RUNNING')
    def running(self, sender):
        self.noteifier.resume() if sender.title == 'Status: PAUSED' else self.noteifier.pause()
        sender.title = 'Status: RUNNING' if sender.title == 'Status: PAUSED' else 'Status: PAUSED'

    @rumps.clicked('New Note')
    def note(self, sender):
        sender.title = 'New Note'
        window = rumps.Window(title='New Note', cancel=True, ok="IGNORE ME")
        window.add_buttons(monitored_applications.keys())
        response = window.run()
        if response.clicked not in {0, 1}:
            app_name = list(monitored_applications)[response.clicked-2]
            tools.new_note(app_name, response.text, self.currdir)


if __name__ == '__main__':
    NoteifierApp().run()
