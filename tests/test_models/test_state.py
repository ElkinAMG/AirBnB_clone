#!/usr/bin/python3
"""
Unittesting for `State`.
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class StateTest(unittest.TestCase):
    """
    Testing Class for `State`
    """

    def test_name(self):
        """Checks type of name"""
        self.assertEqual(type(State.name), str)

    def pep8(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/user.py", "test/test_models/test_user.py"])
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')
