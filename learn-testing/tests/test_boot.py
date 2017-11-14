#! /usr/bin/python
# -*- coding: utf-8 -*-

# Python standard libraries
import logging
import sys

# Python 3rd-part libraries
import wx

# Project modules
from app.easyconfig.wxapp import WxApp

# Modules for debugging
import unittest


class MyDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'Test')
        wx.Button(self, wx.ID_OK)
        self.testo = wx.TextCtrl(parent=self)


class TestMyDialog(unittest.TestCase):

    def setUp(self):
        self.easy_config = WxApp()

        page_id = self.easy_config.tabbed_pages["stations"].index("site")
        #targeted_button = self.easy_config.top_frame.apps_panels["stations"].notebook.GetPage(page_id).customized_panel.widgetry_panel._widgets['commands']['CRUD_new'].GetLabel()
        app_panel = self.easy_config.top_frame.apps_panels["stations"]
        widgetry_panel = app_panel.notebook.GetPage(page_id).customized_panel.widgetry_panel

        self._targeted_button = widgetry_panel._widgets['commands']['CRUD_new']
        self.widgetry_panel = widgetry_panel

    def tearDown(self):
        self.easy_config.OnExit()

    def _rst(self):
        return self.easy_config.present_recordsets.recordset(
            app_name="stations", model_name="site"
        )

    def testNewSite(self):
        def clickAddOne():
            event = wx.CommandEvent(
                wx.wxEVT_COMMAND_BUTTON_CLICKED,
                self._targeted_button.GetId()
            )
            self._targeted_button.GetEventHandler().ProcessEvent(event)
            self.widgetry_panel.dialog.name_widget.SetValue("Milan")

        print self._targeted_button.GetLabel()
        print len(self._rst())
        wx.CallAfter(clickAddOne)
        print self._rst()
        self.assertEqual("ciao", "ciao", msg="Sbagliato")


    def runTest(self):
        self.testNewSite()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMyDialog())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)