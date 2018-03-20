from models.constants import monitored_applications
from handlers.tools import app_to_name
from noteifier import Noteifier
from threading import Thread
import random
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
    def meh(self, sender):
        sender.title = 'New Note'
        response = rumps.Window(title='New Note', message="Please include your desired application tag.", cancel=True).run()
        if response.clicked:
            # THIS HAS ISSUES, DOESNT ACTUALLY OPEN THE RIGHT DIRECTORY
            files = os.listdir(self.currdir + '/Documents')
            num = str(random.randint(0,10000)) + '.txt'
            print(num)
            while num in files:
                num = str(random.randint(0,10000)) + '.txt'
                print(num)
            with open(self.currdir + '/Documents/{}.txt'.format(num), 'w') as f:
                f.write(response.text)


if __name__ == '__main__':
    NoteifierApp().run()
