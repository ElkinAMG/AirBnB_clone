"""
Unittesting for `City`.
"""
import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel


class CityTest(unittest.TestCase):
    """
    Testing Class for `City`
    """

    def test_state_id(self):
        """Checks type of email"""

        self.assertEqual(type(City.state_id), str)

    def test_name(self):
        """Checks type of password"""
        self.assertEqual(type(City.name), str)

    def test_documentation(self):
        """Checks the documentation of City class"""
        doc = City.__doc__
        self.assertGreaterEqual(len(doc), 1)

    def pep8(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/user.py", "test/test_models/test_user.py"])
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')
