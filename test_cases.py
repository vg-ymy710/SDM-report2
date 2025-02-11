#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # 有効範囲内でのテスト
        def test_sample1 (self):
                self.assertEqual (1, calc(1, 1))

        def test_sample2 (self):
                self.assertEqual (998001, calc(999, 999))

        def test_sample3 (self):
                self.assertEqual (999, calc(1, 999))

        def test_sample4 (self):
                self.assertEqual (999, calc(999, 1))

        # 無効な値である０が渡された場合
        def test_sample5 (self):
                self.assertEqual (-1, calc(0, 500))

        def test_sample6 (self):
                self.assertEqual (-1, calc(500, 0))

        # 無効な値である1000が入力された場合
        def test_sample7 (self):
                self.assertEqual (-1, calc(1000, 500))

        def test_sample8 (self):
                self.assertEqual (-1, calc(500, 1000))

        # 無効な入力として文字列が与えられた場合
        def test_sample9 (self):
                self.assertEqual (-1, calc("100", 500))
        
        def test_sample10 (self):
                self.assertEqual (-1, calc(500, "100"))

        # 無効な値として小数が与えられた場合
        def test_sample11 (self):
                self.assertEqual (-1, calc(1.1, 500))

        def test_sample12 (self):
                self.assertEqual (-1, calc(500, 1.1))