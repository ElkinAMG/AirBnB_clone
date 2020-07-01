"""
Unittesting for `Review`.
"""
import unittest
from models.review import Review
from models.place import Place
from models.user import User


class UserTest(unittest.TestCase):
    """
    Testing Class for `Review`
    """

    def test_place_id(self):
        """Checks type of place_id"""
        place = Place()
        rev = Review()
        rev.place_id = place.id
        self.assertEqual(type(rev.place_id), str)

    def test_user_id(self):
        """Checks type of user_id"""
        user = User()
        rev = Review()
        rev.user_id = user.id
        self.assertEqual(type(rev.user_id), str)

    def test_text(self):
        """Checks type of text"""
        rev = Review()
        rev.text = "Estuvo vacilable ese motel valecita!!"
        self.assertEqual(type(rev.user_id), str)

    def pep8(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/user.py", "test/test_models/test_user.py"])
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')
