#!/usr/bin/env python3

from FirstModule import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Davis, Scott"
        expected = "Scott Davis"
        self.assertEqual(rearrange_name(testcase),expected)
        
    
unittest.create_body_para()

