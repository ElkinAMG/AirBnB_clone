"""
Unittesting for `Place`.
"""
import unittest
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel

class PlaceTest(unittest.TestCase):
    """
    Testing Class for `Place`
    """

    def setUp(self):
        """set up a Place class model"""
        self.ins = Place()
        self.ins.city_id = "Barranquilla"
        self.ins.user_id = "1234-1234-abcd-1234"
        self.ins.name = "Andrew"
        self.ins.description = "Christmas holiday stay"
        self.ins.number_rooms = 2
        self.ins.number_bathrooms = 2
        self.ins.max_guest = 6
        self.ins.price_by_night = 55
        self.ins.latitude = 10.5
        self.ins.longitude = 89.3
        self.new_amenity = Amenity()
        self.ins.amenity_ids = [self.new_amenity.id, self.new_amenity.id]
        self.list = [
            "__init__", "__str__", "save", "to_dict", "city_id", "user_id",
            "name", "description", "number_rooms", "number_bathrooms",
            "max_guest", "price_by_night", "latitude", "longitude",
            "amenity_ids", "id", "created_at", "updated_at"
        ]
        self.list_int = [
            "number_rooms", "number_bathrooms",
            "max_guest", "price_by_night"
        ]
        self.list_float = [
            "latitude", "longitude"
        ]

    def test_hasattr(self):
        """check if Place model has the required attributes"""
        for i in self.list:
            self.assertTrue(hasattr(self.ins, i))

    def test_dub_instance(self):
        """check if class is subinstance of BaseClass"""
        self.assertTrue(issubclass(type(self.ins), BaseModel))

    def test_doc_string(self):
        """testing if docstrings exist"""
        self.assertEqual(len(Place.__doc__) > 0, True)
        self.assertEqual(len(Place.__init__.__doc__) > 0, True)
        self.assertEqual(len(Place.__str__.__doc__) > 0, True)
        self.assertEqual(len(Place.save.__doc__) > 0, True)
        self.assertEqual(len(Place.to_dict.__doc__) > 0, True)

    def test_instance(self):
        """testing to see whether created instance is equal to Place"""
        self.assertTrue(isinstance(self.ins, Place))
        self.assertTrue(self.ins.__class__ == Place)

    def test_save_method(self):
        """testig whether save methd works for Place"""
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        with open("file.json", "r") as f:
            lines = f.read()
            self.assertTrue(len(lines) > 0)

    def test_to_dict(self):
        """test to dict method of Place"""
        dic = self.ins.to_dict()
        self.assertTrue(len(dic) > 0)
        self.assertTrue(isinstance(dic, dict))
        for k, v in dic.items():
            if k in self.list_int:
                self.assertTrue(isinstance(dic[k], int))
            elif k in self.list_float:
                self.assertTrue(isinstance(dic[k], float))
            elif k == "amenity_ids":
                self.assertTrue(isinstance(dic[k], list))
            else:
                self.assertTrue(isinstance(dic[k], str))

    def test_str_method(self):
        """test whether the string method returns the correct output"""
        uid = self.ins.id
        cl_name = self.ins.__class__.__name__
        dic = self.ins.__dict__
        self.assertEqual(self.ins.__str__(), "[{}] ({}) {}".format(cl_name, uid, dic))

    def test_update(self):
        """test whether the update method updates an object properly"""
        new = Place(**(self.ins.to_dict()))
        for k, v in new.to_dict().items():
            self.assertEqual(new.to_dict()[k], self.ins.to_dict()[k])