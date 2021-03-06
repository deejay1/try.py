#!/usr/bin/python
# coding: utf-8

import unittest
import os


# write solution here

class DoogieTest(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def testLog(self):
        os.unlink("/tmp/output")
        example = "sometest"
        self.logger.log(example)
        self.logger.log(example)
        self.assertEquals(open("/tmp/output", "r").read(), example + "\n" + example + "\n")
