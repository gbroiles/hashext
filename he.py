#! /usr/bin/env python3
import argparse
import datetime
import os
import random
import sys
import hashlib
import wx

target = ""


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((432, 414))
        self.list = wx.ListCtrl(self, wx.ID_ANY, style=wx.FULL_REPAINT_ON_RESIZE | wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        global target
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(target)
        self.list.SetMinSize((-1, -1))
        self.list.AppendColumn("Item", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list.AppendColumn("Value", format=wx.LIST_FORMAT_LEFT, width=-1)
#        self.list.EnableAlternateRowColours(True)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.list, 3, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.Many_Hash(target)
        self.frame.Show()
        return True

    def OnQuit(self, e):
        self.Close()

    def Many_Hash(self, filename):
        global target
        filename = target
        with open(filename, "rb") as f:
            data = f.read()
        md5 = hashlib.md5(data).hexdigest()
        sha1 = hashlib.sha1(data).hexdigest()
        sha256 = hashlib.sha256(data).hexdigest()
        sha512 = hashlib.sha512(data).hexdigest()
        self.frame.list.Append(["size:", "{:,}".format(len(data))])
        self.frame.list.Append(["md5:", md5.upper()])
        self.frame.list.Append(["sha1:", sha1.upper()])
        self.frame.list.Append(["sha256:", sha256.upper()])
        self.frame.list.Append(["sha512:", sha512.upper()])
        self.frame.list.SetColumnWidth(0,-1)
        self.frame.list.SetColumnWidth(1,-1)
        self.frame.SetSize(self.frame.list.GetColumnWidth(0) + self.frame.list.GetColumnWidth(1) + 12, 135)


# end of class MyApp

def main():
    global target
    parser = create_parse()
    args = parser.parse_args()
    target = args.target
    app = MyApp(0)
    app.MainLoop()


def create_parse():
    """ set up parser options """
    parser = argparse.ArgumentParser(description="file hashing shell extension")
    parser.add_argument("target", help="file to be hashed")
    return parser

if __name__ == "__main__":
    main()
