from handlers import tools
import wx
import os


# (Heavy) Reference: https://stackoverflow.com/questions/42796950/python-using-wxpython-to-get-multiple-input-from-user
class NewNoteDialog(wx.Dialog):

    def __init__(self, parent, noteifier):
        self.noteifier = noteifier

        wx.Dialog.__init__(self, parent, wx.ID_ANY, "New Note", size=(400, 300), style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.lblapp = wx.StaticText(self.panel, label="Application", pos=(20, 20))
        self.app = wx.TextCtrl(self.panel, value="", pos=(110, 20), size=(270, -1))

        self.lblnote = wx.StaticText(self.panel, label="Note", pos=(20, 60))
        self.note = wx.TextCtrl(self.panel, value="", pos=(110, 60), size=(270, 150))

        self.saveButton = wx.Button(self.panel, label="Save", pos=(110, 220))
        self.cancelButton = wx.Button(self.panel, label="Cancel", pos=(210, 220))

        self.saveButton.Bind(wx.EVT_BUTTON, self.save_note)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.on_quit)

        self.lblerror = wx.StaticText(self.panel, label="", pos=(20, 280))

        self.Bind(wx.EVT_CLOSE, self.on_quit)

        self.Show()

    def on_quit(self, event):
        self.Destroy()

    def save_note(self, event):
        if self.app.GetValue() not in self.noteifier.monitored_applications:
            self.lblerror.Destroy()
            self.lblerror = wx.StaticText(self.panel, label='ERROR: Application name not found.', pos=(110, 250))
            self.lblerror.SetForegroundColour((255, 0, 0))
        elif not self.note.GetValue():
            self.lblerror.Destroy()
            self.lblerror = wx.StaticText(self.panel, label='ERROR: No note to save.', pos=(110, 250))
            self.lblerror.SetForegroundColour((255, 0, 0))
        else:
            tools.new_note(self.app.GetValue(), self.note.GetValue(), os.getcwd())
            self.Destroy()
