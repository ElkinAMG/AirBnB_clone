#!/usr/bin/python3
"""
Unittesting for `State`.
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from time import sleep
from datetime import datetime


class StateTest(unittest.TestCase):
    """
    Testing Class for `User`
    """

    def setUp(self):
        """set up a user class model"""
        self.ins = State()
        self.ins.name = "Malambo"

    def test_hasattr(self):
        """check if user model has the required attributes"""
        self.assertTrue(hasattr(self.ins, "__init__"))
        self.assertTrue(hasattr(self.ins, "__str__"))
        self.assertTrue(hasattr(self.ins, "save"))
        self.assertTrue(hasattr(self.ins, "to_dict"))
        self.assertTrue(hasattr(self.ins, "name"))

    def tes_dub_instance(self):
        """check if class is subinstance of BaseClass"""
        self.assertTrue(issubclass(type(self.ins), BaseModel))

    def test_doc_string(self):
        """testing if docstrings exist"""
        self.assertEqual(len(State.__doc__) > 0, True)
        self.assertEqual(len(State.__init__.__doc__) > 0, True)
        self.assertEqual(len(State.__str__.__doc__) > 0, True)
        self.assertEqual(len(State.save.__doc__) > 0, True)
        self.assertEqual(len(State.to_dict.__doc__) > 0, True)

    def test_instance(self):
        """testing to see whether created instance is equal to State"""
        self.assertTrue(isinstance(self.ins, State))
        self.assertTrue(self.ins.__class__ == State)

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        sleep(1)

        now = datetime.now().replace(microsecond=0)
        obj.save()

        self.assertEqual(obj.updated_at.replace(microsecond=0),
                         now)

    def test_save_state(self):
        """testig whether save methd works for State"""
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
        new = State(**(self.ins.to_dict()))
        for k, v in new.to_dict().items():
            self.assertEqual(new.to_dict()[k], self.ins.to_dict()[k])
