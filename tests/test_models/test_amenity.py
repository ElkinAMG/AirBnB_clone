"""
Unittesting for `State`.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """
    Testing Class for `Amenity`
    """

    def test_name(self):
        """Checks type of password"""
        self.assertEqual(type(Amenity.name), str)

    def test_documentation(self):
        """Checks the documentation of Amenity class"""
        doc = Amenity.__doc__
        self.assertGreaterEqual(len(doc), 1)

    def pep8(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/user.py", "test/test_models/test_user.py"])
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')
