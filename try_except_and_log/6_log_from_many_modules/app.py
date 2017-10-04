#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
import logging
import unittest

# Python 3rd-part libraries
import wx

# Project modules


# Modules only for debugging
from pprint import pprint


class WxApp(wx.App):
    def OnInit(self):
        print 'OnInit', self
        self.top_frame = wx.Frame(None, -1, "Some Frame")
        self.top_frame.Show()
        return True

    def OnExit(self):
        print 'OnExit'
        self.top_frame.Destroy()


class TestExample(unittest.TestCase):
    def setUp(self):
        # Scrivo righe analoghe alla __if__name=='__main__' di crud.py
        # ma ometto la 'mainLoop'.
        self.app = WxApp()

    def tearDown(self):
        self.app.OnExit()

    def testSomething(self):
        logger = logging.getLogger(__name__)
        logger.info("sono dal lato unittest")
        print 'testing something...'
        self.assertEqual("valore", "valore", msg="non appaio mai!")

    def runTest(self):
        self.testSomething()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)