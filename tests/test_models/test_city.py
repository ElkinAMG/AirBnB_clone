"""
Unittesting for `User`.
"""
import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel


class UserTest(unittest.TestCase):
    """
    Testing Class for `User`
    """

    def setUp(self):
        """set up a user class model"""
        self.ins = City()
        self.state = State()
        self.ins.state_id = self.state.id
        self.ins.name = "Barranquilla"

    def test_hasattr(self):
        """check if user model has the required attributes"""
        self.assertTrue(hasattr(self.ins, "__init__"))
        self.assertTrue(hasattr(self.ins, "__str__"))
        self.assertTrue(hasattr(self.ins, "save"))
        self.assertTrue(hasattr(self.ins, "to_dict"))
        self.assertTrue(hasattr(self.ins, "state_id"))
        self.assertTrue(hasattr(self.ins, "name"))

    def tes_dub_instance(self):
        """check if class is subinstance of BaseClass"""
        self.assertTrue(issubclass(type(self.ins), BaseModel))

    def test_doc_string(self):
        """testing if docstrings exist"""
        self.assertEqual(len(City.__doc__) > 0, True)
        self.assertEqual(len(City.__init__.__doc__) > 0, True)
        self.assertEqual(len(City.__str__.__doc__) > 0, True)
        self.assertEqual(len(City.save.__doc__) > 0, True)
        self.assertEqual(len(City.to_dict.__doc__) > 0, True)

    def test_instance(self):
        """testing to see whether created instance is equal to User"""
        self.assertTrue(isinstance(self.ins, City))
        self.assertTrue(self.ins.__class__ == City)

    def test_save_method(self):
        """testig whether save methd works for User"""
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        with open("file.json", "r") as f:
            lines = f.read()
            self.assertTrue(len(lines) > 0)

    def test_to_dict(self):
        """test to dict method of user"""
        dic = self.ins.to_dict()
        self.assertTrue(len(dic) > 0)
        self.assertTrue(isinstance(dic, dict))
        for k, v in dic.items():
            if k != "__class__":
                self.assertTrue(isinstance(dic[k], str))

    def test_str_method(self):
        """test whether the string method returns the correct output"""
        uid = self.ins.id
        cl_name = self.ins.__class__.__name__
        dic = self.ins.__dict__
        self.assertEqual(self.ins.__str__(),
                         "[{}] ({}) {}".format(cl_name, uid, dic))

    def test_update(self):
        """test whether the update method updates an object properly"""
        new = City(**(self.ins.to_dict()))
        for k, v in new.to_dict().items():
            self.assertEqual(new.to_dict()[k], self.ins.to_dict()[k])
