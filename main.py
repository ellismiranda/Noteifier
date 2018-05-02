import wx
from models.NoteifierApp import NoteifierApp


if __name__ == "__main__":
    app = wx.App()
    NoteifierApp()
    app.MainLoop()