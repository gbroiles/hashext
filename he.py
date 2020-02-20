#! /usr/bin/env python3
import argparse
import datetime
import os
import random
import sys
import hashlib
import wx

target = ""


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(mainWindow, self).__init__(
            parent, title=title, style=wx.DEFAULT_FRAME_STYLE, size=(400, 300)
        )
        self.Centre()
        self.InitUI()

    def InitUI(self):
        global target
        #        self.CreateStatusBar()

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(0, 0)

        st1 = wx.StaticText(panel, label="Target:")
        sizer.Add(
            st1,
            pos=(0, 0),
            flag=wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
            border=5,
        )

        self.targetname = wx.TextCtrl(panel)
        self.targetname.SetValue(str(target))
        sizer.Add(
            self.targetname,
            pos=(0, 1),
            span=(1, 3),
            flag=wx.ALL | wx.ALIGN_LEFT,
            border=5,
        )

        self.report = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer.Add(
            self.report, pos=(2, 2), flag=wx.EXPAND | wx.ALL, border=5,
        )

        sizer.AddGrowableRow(2)

        panel.SetSizer(sizer)

        self.Many_Hash(target)

    def OnQuit(self, e):
        self.Close()

    def Many_Hash(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        md5 = hashlib.md5(data).hexdigest()
        sha1 = hashlib.sha1(data).hexdigest()
        sha256 = hashlib.sha256(data).hexdigest()
        sha512 = hashlib.sha512(data).hexdigest()
        self.report.AppendText("size: {:,}\n".format(len(data)))
        self.report.AppendText("md5: {}\n".format(md5))
        self.report.AppendText("sha1: {}\n".format(sha1))
        self.report.AppendText("sha256: {}\n".format(sha256))
        self.report.AppendText("sha512: {}\n".format(sha512))


def main():
    global target
    parser = create_parse()
    args = parser.parse_args()
    target = args.target
    print("target = {}".format(target))
    app = wx.App()
    frame = mainWindow(None, title="Hash utility")
    frame.Show()
    app.MainLoop()


def create_parse():
    """ set up parser options """
    parser = argparse.ArgumentParser(description="file hashing shell extension")
    parser.add_argument("target", help="file to be hashed")
    return parser


if __name__ == "__main__":
    main()
