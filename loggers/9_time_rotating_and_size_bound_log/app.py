#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
import inspect
import unittest

# Python 3rd-part libraries
import wx

# Project modules
from logging_ import (
    dev_logger,
    dist_logger,
)

# Modules only for debugging
from pprint import pprint


def log_call(self):
    dev_logger.debug(
        "{}::{}".format(
            inspect.stack()[0][3], str(self),
        )
    )


class WxApp(wx.App):
    def OnInit(self):
        log_call(self)
        self.top_frame = wx.Frame(None, -1, "Some Frame")
        self.top_frame.Show()
        return True

    def OnExit(self):
        log_call(self)
        self.top_frame.Destroy()


class TestExample(unittest.TestCase):
    def setUp(self):
        # Scrivo righe analoghe alla __if__name=='__main__' di crud.py
        # ma ometto la 'mainLoop'.
        log_call(self)
        self.app = WxApp()

    def tearDown(self):
        log_call(self)
        self.app.OnExit()

    def testSomething(self):
        log_call(self)
        dev_logger.info("sto facendo dei test...")
        dist_logger.info("sto facendo dei test...")
        self.assertEqual("valore", "valore", msg="non appaio mai!")

    def runTest(self):
        log_call(self)
        self.testSomething()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample())
    return suite


def run_suite():
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)


if __name__ == '__main__':
    run_suite()