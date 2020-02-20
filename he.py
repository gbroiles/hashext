#! /usr/bin/env python3
import datetime
import os
import random
import sys
import hashlib
import wx


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(mainWindow, self).__init__(
            parent, title=title, style=wx.DEFAULT_FRAME_STYLE, size=(250, 300)
        )
        self.Centre()
        self.InitUI()

    def InitUI(self):
        self.CreateStatusBar()

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(2, 3)

        st1 = wx.StaticText(panel, label="Target:")
        sizer.Add(
            st1,
            pos=(0, 0),
            flag=wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
            border=5,
        )

        self.targetname = wx.TextCtrl(panel)
        sizer.Add(self.targetname, pos=(0, 1), span=(1, 4), flag=wx.ALL | wx.ALIGN_LEFT, border=5)

        self.report = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer.Add(
            self.report,
            pos=(2, 0),
            span=(0, 3),
            flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
            border=5,
        )

        sizer.AddGrowableRow(2)

        panel.SetSizer(sizer)

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    frame = mainWindow(None, title="Hash utility")
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
