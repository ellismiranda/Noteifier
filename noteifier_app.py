from noteifier import Noteifier
from threading import Thread
from handlers import tools
import rumps
import os


class NoteifierApp(rumps.App):
    def __init__(self):
        super(NoteifierApp, self).__init__("Test App")
        self.currdir = str(os.getcwd())
        self.icon = 'assets/icon.png'
        self.menu = ['Status: RUNNING', 'New Note']
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
        response = rumps.Window(title='New Note', message="Please include your desired application tag.", cancel=True).run()
        if response.clicked:
            tools.new_note(response.text, self.currdir)


if __name__ == '__main__':
    NoteifierApp().run()
