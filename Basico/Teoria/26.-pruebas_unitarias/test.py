# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h9noCb-Mi-yfqezot0nIeL9AId_wR4Sw

# **Unit Testing**

The unit testing in a programmin language consist in proof each part o module of te written code.

In Python we have some libraries to do this like , unittest, doctest, ect, but today we are going to use **unittest**

- ## **unittest Methods**

|  Method                     |  Proof that 
|-----------------------------|--------------
| assertEqual(a,b)            |  a == b
| assertNoEqual(a, b)         |  a != b
| assertTrue(x)               |  bool(x) is True
| assertFalse(x)              |  bool(x) us False
| assertIs(a, b)              |  a is b
| assertIsNot(a,b)            |  a is not b
| assertIsNone(x)             |  x is None
| asserIsNotNone              |  x is not None
| assertIn(a, b)              |  a in b
| assertNotIn(a, b)           |  a ot in b
| assertIsInstance(a, b)      |  isinstance(a, b)
| assertNotIsInstance(a, b)   |  not isinstance(a, b)
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd drive/MyDrive/Basic\ Python/"18.-unit_test"

import unittest

import calc

class TestCalc( unittest.TestCase ):

    def test_add(self):

        addition_result = calc.get_add(12, 4)

        self.assertEqual( addition_result, 16 )
        self.assertEqual( calc.get_add(2, 3), 6 )

    def test_substract(self):

        self.assertEqual( calc.get_substract(12, 45), -33 )

    def test_multiply(self):

        self.assertEqual( calc.get_multiply(3, 5), 15 )

    def test_divide(self):

        self.assertEqual( calc.get_divide(34, 4), 6 )

