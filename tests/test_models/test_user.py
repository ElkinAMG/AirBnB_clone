#!/usr/bin/python3
"""
Unittesting for `User`.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class UserTest(unittest.TestCase):
    """
    Testing Class for `User`
    """

    def setUp(self):
        """set up a user class model"""
        self.ins = User()
        self.ins.email = "andrew_kalil@gmail.com"
        self.ins.password = "tryHarderf00l"
        self.ins.first_name = "Andrew"
        self.ins.last_name = "Kalil"

    def test_hasattr(self):
        """check if user model has the required attributes"""
        self.assertTrue(hasattr(self.ins, "__init__"))
        self.assertTrue(hasattr(self.ins, "__str__"))
        self.assertTrue(hasattr(self.ins, "save"))
        self.assertTrue(hasattr(self.ins, "to_dict"))
        self.assertTrue(hasattr(self.ins, "email"))
        self.assertTrue(hasattr(self.ins, "password"))
        self.assertTrue(hasattr(self.ins, "first_name"))
        self.assertTrue(hasattr(self.ins, "last_name"))
        self.assertTrue(hasattr(self.ins, "id"))
        self.assertTrue(hasattr(self.ins, "created_at"))
        self.assertTrue(hasattr(self.ins, "updated_at"))

    def test_dub_instance(self):
        """check if class is subinstance of BaseClass"""
        self.assertTrue(issubclass(type(self.ins), BaseModel))

    def test_doc_string(self):
        """testing if docstrings exist"""
        self.assertEqual(len(User.__doc__) > 0, True)
        self.assertEqual(len(User.__init__.__doc__) > 0, True)
        self.assertEqual(len(User.__str__.__doc__) > 0, True)
        self.assertEqual(len(User.save.__doc__) > 0, True)
        self.assertEqual(len(User.to_dict.__doc__) > 0, True)

    def test_instance(self):
        """testing to see whether created instance is equal to User"""
        self.assertTrue(isinstance(self.ins, User))
        self.assertTrue(self.ins.__class__ == User)

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
        self.assertEqual(self.ins.__str__(), "[{}] ({}) {}".format(cl_name, uid, dic))

    def test_update(self):
        """test whether the update method updates an object properly"""
        new = User(**(self.ins.to_dict()))
        self.assertEqual(self.ins.id, new.id)
        self.assertEqual(self.ins.updated_at, new.updated_at)
        self.assertEqual(self.ins.created_at, new.created_at)
