from threading import Thread
from noteifier import Noteifier
import rumps


class TestMenuBarApp(rumps.App):
    def __init__(self):
        super(TestMenuBarApp, self).__init__("Test App")
        self.icon = 'assets/icon.png'
        self.menu = ['Status: RUNNING', 'New Note']
        self.noteifier = Noteifier()
        self.monitor = Thread(target=self.noteifier.run,)
        self.monitor.start()

    @rumps.clicked('Status: RUNNING')
    def running(self, sender):
        self.noteifier.resume() if sender.title == 'PAUSED' else self.noteifier.pause()
        sender.title = 'Status: RUNNING' if sender.title == 'Status: PAUSED' else 'Status: PAUSED'

    # @rumps.clicked('New Note')
    # def button(self):
    #     new_note = rumps.Window("New Note").run()


if __name__ == '__main__':
    TestMenuBarApp().run()