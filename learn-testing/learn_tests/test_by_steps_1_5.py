# -*- coding: utf-8 -*-

"""
La cosa importante messa in luce da questo codice
è che
"""


import unittest
import wx

class MyDialog(wx.Dialog):
    def __init__(self, parent):
        print '4 MyDialog.__init__'
        wx.Dialog.__init__(self, parent, -1, 'Test')
        self.text_widget = wx.TextCtrl(parent=self)
        wx.Button(self, wx.ID_OK)

class TestMyDialog(unittest.TestCase):

    def setUp(self):
        print '1 setUp'
        self.app = wx.App()
        self.frame = wx.Frame(None)
        self.frame.Show()

    def tearDown(self):
        print 'tearDown'
        wx.CallAfter(self.app.Exit)
        self.app.MainLoop()

    def testDialog(self):
        print '2 testDialog'
        def clickOK():
            print '5\tclickOK'
            clickEvent = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, wx.ID_OK)
            self.dialog.ProcessEvent(clickEvent)
        print 'ora call after'
        wx.CallAfter(clickOK)
        print 'ora show dialog'
        self.ShowDialog()

    def ShowDialog(self):
        print '3 ShowDialog'
        self.dialog = MyDialog(self.frame)
        self.dialog.text_widget.SetValue("Pergocrema")
        print 'ora show modal'
        self.dialog.ShowModal()
        print 'ora destroy'
        self.dialog.Destroy()

if __name__ == '__main__':
    print '0 __main__'
    unittest.main()
