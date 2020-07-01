#!/usr/bin/python3
"""
Unittesting for `User`.
"""
import unittest
from models.user import User
import pep8


class UserTest(unittest.TestCase):
    """
    Testing Class for `User`
    """

    def test_email(self):
        """Checks type of email"""

        self.assertEqual(type(User.email), str)

    def test_password(self):
        """Checks type of password"""
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        """Checks type of first_name"""
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """Checks type of last_name"""
        self.assertEqual(type(User.last_name), str)

    def test_documentation(self):
        """Checks the documentation of User class"""
        doc = User.__doc__
        self.assertGreaterEqual(len(doc), 1)

    def pep8(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/user.py", "test/test_models/test_user.py"])
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')
