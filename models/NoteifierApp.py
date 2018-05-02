# (Heavy) Reference: https://stackoverflow.com/questions/6389580/quick-and-easy-trayicon-with-python
from models.noteifier import Noteifier
from threading import Thread
from models import NewNoteDialog, NewApplicationDialog
from wx import adv
import wx
import os

TRAY_TOOLTIP = 'Noteifier'
TRAY_ICON = 'assets/icon_new.png'


class NoteifierTaskBar(adv.TaskBarIcon):
    def __init__(self,frame):
        adv.TaskBarIcon.__init__(self)
        self.currdir = str(os.getcwd())
        self.app_frame = frame
        self.SetIcon(wx.Icon(TRAY_ICON), TRAY_TOOLTIP)
        self.Bind(adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

        self.noteifier = Noteifier()
        self.monitor = Thread(target=self.noteifier.run,)
        self.monitor.start()

    def CreatePopupMenu(self):
        self.menu = wx.Menu()

        self.menustatus = wx.MenuItem(self.menu, -1, "Status: RUNNING")
        self.menu.Bind(wx.EVT_MENU, self.running, id=self.menustatus.GetId())
        self.menu.Append(self.menustatus)

        self.menunewnote = wx.MenuItem(self.menu, -1, "New Note")
        self.menu.Bind(wx.EVT_MENU, self.new_note, id=self.menunewnote.GetId())
        self.menu.Append(self.menunewnote)

        self.menunewapp = wx.MenuItem(self.menu, -1, "New Monitor")  # fuckin' change this name it's dumb
        self.menu.Bind(wx.EVT_MENU, self.new_app, id=self.menunewapp.GetId())
        self.menu.Append(self.menunewapp)

        self.menu.AppendSeparator()

        self.menuexit = wx.MenuItem(self.menu, -1, "Exit")
        self.menu.Bind(wx.EVT_MENU, self.on_exit, id=self.menuexit.GetId())
        self.menu.Append(self.menuexit)

        return self.menu

    def on_left_down(self, event):
        pass

    def running(self, event):
        # print(self.menustatus.GetLabel())
        # self.menustatus.SetItemLabel("running")
        # self.menu.UpdateUI(self.app_frame)
        pass

    def new_note(self, event):
        NewNoteDialog.NewNoteDialog(None)

    def new_app(self, event):
        NewApplicationDialog.NewApplicationDialog(None)

    def on_exit(self, event):
        self.app_frame.Close()


class NoteifierApp(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(1, 1))
        panel = wx.Panel(self)
        self.app = NoteifierTaskBar(self)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        self.app.noteifier.pause()
        self.app.RemoveIcon()
        self.app.Destroy()
        self.Destroy()
