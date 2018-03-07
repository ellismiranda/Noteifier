from threading import Thread
from noteifier import Noteifier
import rumps


class TestMenuBarApp(rumps.App):
    def __init__(self):
        super(TestMenuBarApp, self).__init__("Test App")
        self.icon = 'assets/icon.png'
        self.menu = ['RUNNING',]
        self.noteifier = Noteifier()
        self.monitor = Thread(target=self.noteifier.run,)
        self.monitor.start()

    @rumps.clicked('RUNNING')
    def running(self, sender):
        self.noteifier.resume() if sender.title == 'PAUSED' else self.noteifier.pause()
        sender.title = 'RUNNING' if sender.title == 'PAUSED' else 'PAUSED'
        

if __name__ == '__main__':
    TestMenuBarApp().run()