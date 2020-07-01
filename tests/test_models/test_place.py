"""
Unittesting for `Place`.
"""
import unittest
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from time import sleep
from datetime import datetime


class PlaceTest(unittest.TestCase):
    """
    Testing Class for `Place`
    """

    def test_city_id(self):
        """Checks type of city_id"""

        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """Checks type user_id"""
        self.assertEqual(type(Place.user_id), str)

    def test_name(self):
        """Checks type of name"""
        self.assertEqual(type(Place.name), str)

    def test_description(self):
        """Checks type of description"""
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """check type of number_rooms"""
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_nathrooms(self):
        """check type of number_bathrooms"""
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guests(self):
        """check type of max_guests"""
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """check type of price_by_night"""
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        """check type of latitude"""
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """check type of longitude"""
        self.assertEqual(type(Place.longitude), float)

    def test_aminity_ids(self):
        """check type of aminity_ids"""
        self.assertEqual(type(Place.amenity_ids), list)

    def test_documentation(self):
        """Checks the documentation of Place class"""
        doc = Place.__doc__
        self.assertGreaterEqual(len(doc), 1)

    def pep8(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/user.py", "test/test_models/test_user.py"])
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')
