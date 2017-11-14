#! /usr/bin/python
# -*- coding: utf-8 -*-


# Python standard libraries

# Python 3rd-part libraries
import wx

# Project modules
from app import (
    WxApp,
)

# Modules for testing
import unittest

class TestMyDialog(unittest.TestCase):

    def setUp(self):
        print '\n\n\nsetUp'

        self.app = WxApp()



        print '\n'

    def tearDown(self):
        print 'teardown'
        pass
        #wx.CallAfter(self.app.Exit)
        self.app.MainLoop()

        """
        print 'tearDown'
        """

    def testAltro(self):
        self.assertTrue('FOO'.isupper())

    def testAddOne(self):
        btn = self.app.top_frame.new_widget

        def clickOk():
            print '\tinner'
            dlg = wx.GetActiveWindow()
            print dlg
            dlg.first_name.SetValue("Luka")
            dlg.family_name.SetValue("Modric")
            clickEvent = wx.CommandEvent(
                wx.wxEVT_COMMAND_BUTTON_CLICKED,
                wx.ID_OK
            )
            dlg.ProcessEvent(clickEvent)

        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, btn.GetId())
        wx.CallAfter(clickOk)
        self.app.top_frame.GetEventHandler().ProcessEvent(event)
        print 'faccio il test'
        print self.app.PEOPLE
        self.assertEqual("uno", "uno", msg="no-way!")

if __name__ == '__main__':
    unittest.main()



