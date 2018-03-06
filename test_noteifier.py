from threading import Thread, Event
from noteifier import noteifier
import rumps


class TestMenuBarApp(rumps.App):
    def __init__(self):
        super(TestMenuBarApp, self).__init__("Test App")
        self.icon = 'assets/icon.png'
        self.menu = ['RUNNING',]
        self.paused = Event()
        self.noteifier = Thread(target=noteifier, )
        self.noteifier.start()

    # @rumps.clicked('sup')
    # def sup(self, _):
    #     rumps.alert('hey there')

    @rumps.clicked('RUNNING')
    def running(self, sender):
        self.paused.clear() if sender.title == 'PAUSED' else self.paused.set()
        # DO SOME FUN STUFF WITH THREADS AND CONDITIONS HERE YAY
        sender.title = 'RUNNING' if sender.title == 'PAUSED' else 'PAUSED'


    # @rumps.clicked('ben albert')
    # def benalbert(self, _):
    #     tools.notify(message='there', title='hello', command='\"open ~/Github/Noteifier/assets/icon.png\"')


if __name__ == '__main__':
    TestMenuBarApp().run()