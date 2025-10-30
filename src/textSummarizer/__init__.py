import unittest
if not hasattr(unittest.TestCase, 'assertRaisesRegexp'):
    unittest.TestCase.assertRaisesRegexp = unittest.TestCase.assertRaisesRegex