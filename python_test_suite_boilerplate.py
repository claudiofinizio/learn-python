#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
from collections import OrderedDict
import unittest

# Python 3rd-part libraries
import wx
from wx.lib.pubsub import pub

# Project modules
import crud
from crud import WxApp


# Modules only for debugging
from pprint import pprint


class TestExample(unittest.TestCase):
    def setUp(self):
        # Scrivo righe analoghe alla __if__name=='__main__' di crud.py
        # ma ometto la 'mainLoop'.
        self.app = WxApp()

    def tearDown(self):
        self.app.OnExit()

    def testSomething(self):
        print 'testing...'
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