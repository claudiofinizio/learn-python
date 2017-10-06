#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
import logging
import unittest

# Python 3rd-part libraries
import wx

# Project modules
from logging_ import (
    dev_handler,
    dist_handler,
    dev_logger_factory,
    dist_logger_factory,
)

# Modules only for debugging
from pprint import pprint


# Create loggers.
dev_logger = dev_logger_factory(logger_name='dev_'+__name__)
dist_logger = dist_logger_factory(logger_name='dist'+__name__)


def log_me(func):
    def func_wrapper(*args, **kwargs):
        dist_logger.info("called: {:>20}".format(func.__name__))
        return func(*args, **kwargs)
    return func_wrapper


class WxApp(wx.App):

    @log_me
    def OnInit(self):
        self.top_frame = wx.Frame(None, -1, "Some Frame")
        self.top_frame.Show()
        return True

    @log_me
    def OnExit(self):
        self.top_frame.Destroy()


class TestExample(unittest.TestCase):
    @log_me
    def setUp(self):
        # Scrivo righe analoghe alla __if__name=='__main__' di crud.py
        # ma ometto la 'mainLoop'.
        self.app = WxApp()

    @log_me
    def tearDown(self):
        self.app.OnExit()

    @log_me
    def testSomething(self):
        dev_logger.info("sto facendo dei test...")
        dist_logger.info("sto facendo dei test...")
        self.assertEqual("valore", "valore", msg="non appaio mai!")

    @log_me
    def runTest(self):
        self.testSomething()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample())
    return suite


def run_suite():
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)


run_suite()
if __name__ == '__main__':
    pass