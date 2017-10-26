# -*- coding: utf-8 -*-

import wx

class Frame(wx.Frame):
    def __init__(self, parent):
        super(Frame, self).__init__(parent)

        # 1. Struttura dei widgets.
        self.panel = wx.Panel(parent=self)
        self.text_widget = wx.TextCtrl(parent=self.panel)
        self.save_button = wx.Button(parent=self.panel, label="Save")
        self.load_button = wx.Button(parent=self.panel, label="Load")

        buttons_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        panel_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        text_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        gap_sizer = wx.BoxSizer(orient=wx.VERTICAL)

        text_sizer.Add(self.text_widget, proportion=1)
        buttons_sizer.Add(
            self.save_button, proportion=0, flag = wx.ALIGN_RIGHT,
        )
        buttons_sizer.Add(
            self.load_button, proportion=0, flag = wx.ALIGN_RIGHT,
        )
        gap_sizer.Add(wx.StaticText(parent=self.panel, label=""))
        panel_sizer.Add(text_sizer, proportion=0)
        panel_sizer.Add(gap_sizer, proportion=1, flag=wx.EXPAND)
        panel_sizer.Add(buttons_sizer, proportion=1, flag=wx.ALIGN_RIGHT)
        self.panel.SetSizer(panel_sizer)
        self.panel.Fit()

        # 2. Valori di default
        self.text_widget.SetValue("Riga")
        self.text_widget.SetInsertionPointEnd()

        # 3. Events' binding.
        self.Bind(wx.EVT_BUTTON, self.load, self.load_button)
        self.Bind(wx.EVT_BUTTON, self.save, self.save_button)

        # 4. External file definition.
        self.filename = "grafemi/prova.sql"

    def load(self, event):
        print 'loading...'
        with open(self.filename, "r") as infile:
            stream = infile.read()
            print stream

    def save(self, event):
        print 'saving...'
        with open(self.filename, "a") as outfile:
            outfile.write(self.text_widget.GetValue())


app = wx.App()
frame = Frame(parent=None)
frame.Show()

app.MainLoop()

