"""TEST"""
# pylint: disable=invalid-name
import unittest
from hw5_task import info_python

class test(unittest.TestCase):
    """test class"""

    def test_json_yaml(self):
        """json_yaml"""
        cl = info_python()
        self.assertFalse(cl.creating_json())
        self.assertFalse(cl.creating_yaml())
