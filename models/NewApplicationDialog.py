from models.constants import monitored_applications
from handlers import tools, processes
import wx


class NewApplicationDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Monitor New Process", size=(400, 130), style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.lblapp = wx.StaticText(self.panel, label="Application Name", pos=(10, 20))
        self.app = wx.TextCtrl(self.panel, value="", pos=(130, 20), size=(260, -1))

        self.saveButton = wx.Button(self.panel, label="Save", pos=(165, 70))
        self.cancelButton = wx.Button(self.panel, label="Cancel", pos=(275, 70))

        self.saveButton.Bind(wx.EVT_BUTTON, self.save_app)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.on_quit)

        self.lblerror = wx.StaticText(self.panel, label="The application must be running to begin monitoring.", pos=(10, 47))
        self.lblerror.SetForegroundColour((255, 0, 0))

        self.Bind(wx.EVT_CLOSE, self.on_quit)

        self.Show()

    def on_quit(self, event):
        self.Destroy()

    def save_app(self, event):
        if self.app.GetValue() in monitored_applications:
            self.lblerror.Destroy()
            self.lblerror = wx.StaticText(self.panel, label="Already monitoring {}.".format(self.app.GetValue()), pos=(10, 47))
            self.lblerror.SetForegroundColour((255, 0, 0))
        elif self.app.GetValue() not in processes.parse_application_names(processes.get_active_applications()):
            self.lblerror.Destroy()
            self.lblerror = wx.StaticText(self.panel, label="ERROR: Application not found. Please check spelling.", pos=(10, 47))
            self.lblerror.SetForegroundColour((255, 0, 0))
        else:
            processes.monitor_new_process(self.app.GetValue())
            self.Destroy()
