#! /usr/bin/python
# -*- coding: utf-8 -*-

# Python standard libraries

# Python 3rd-part libraries
import wx

# Project modules

# Modules for debugging
import unittest


class MyDialog(wx.Dialog):
    def __init__(self, parent):
        print 'MyDialog.__init__'
        wx.Dialog.__init__(self, parent, -1, 'Test')
        wx.Button(self, wx.ID_OK)
        self.testo = wx.TextCtrl(parent=self)

class TestMyDialog(unittest.TestCase):

    def setUp(self):
        print 'setUp'
        self.app = wx.App()
        self.frame = wx.Frame(None)
        self.dialog = MyDialog(self.frame)
        self.frame.Show()

    def tearDown(self):
        print 'tearDown'
        wx.CallAfter(self.app.Exit)
        self.app.MainLoop()

    def testDialog(self):
        print 'testDialog'
        def clickOK():
            print '\tclickOK'
            self.dialog.testo.SetValue("molise")
            clickEvent = wx.CommandEvent(
                wx.wxEVT_COMMAND_BUTTON_CLICKED, wx.ID_OK
            )
            self.dialog.ProcessEvent(clickEvent)
            print self.dialog.testo.GetValue()
        wx.CallAfter(clickOK)
        self.ShowDialog()
        self.assertEqual(6, len(self.dialog.testo.GetValue()), msg="Sbagliato")

    def ShowDialog(self):
        print 'ShowDialog'
        self.dialog.ShowModal()
        self.dialog.Destroy()

    def runTest(self):
        print 'runTest'
        self.testDialog()


def suite():
    print 'suite'
    suite = unittest.TestSuite()
    suite.addTest(TestMyDialog())
    return suite


if __name__ == '__main__':
    print '\n\n\n__main__'
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)