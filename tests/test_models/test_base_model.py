#!/usr/bin/python3
"""
Unittesting for `BaseModel`.
"""
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """
    Testing Class for `BaseModel`
    """

    def setUp(self):
        """set up a base class model"""
        self.ins = BaseModel()

    def test_hasattr(self):
        """check if base model has the required attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_doc_string(self):
        """testing if docstrings exist"""
        self.assertEqual(len(BaseModel.__doc__) > 0, True)
        self.assertEqual(len(BaseModel.__init__.__doc__) > 0, True)
        self.assertEqual(len(BaseModel.__str__.__doc__) > 0, True)
        self.assertEqual(len(BaseModel.save.__doc__) > 0, True)
        self.assertEqual(len(BaseModel.to_dict.__doc__) > 0, True)

    def test_instance(self):
        """testing to see whether created instance is equal to BaseModel"""
        self.assertTrue(isinstance(self.ins, BaseModel))
        self.assertTrue(self.ins.__class__ == BaseModel)

    def test_save_method(self):
        """testig whether save methd works for BaseModel"""
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        with open("file.json", "r") as f:
            lines = f.read()
            self.assertTrue(len(lines) > 0)

    def test_to_dict(self):
        """test to dict method of base model"""
        dic = self.ins.to_dict()
        self.assertTrue(len(dic) > 0)
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(dic['created_at'], str))
        self.assertTrue(isinstance(dic['updated_at'], str))
        self.assertTrue(isinstance(dic['id'], str))

    def test_str_method(self):
        """test whether the string method returns the correct output"""

        id = self.ins.id
        cln = self.ins.__class__.__name__
        dic = self.ins.__dict__
        string = self.ins.__str__()
        self.assertEqual(string, "[{}] ({}) {}".format(cln, id, dic))

    def test_update(self):
        """test whether the update method updates an object properly"""
        new = BaseModel(**(self.ins.to_dict()))
        for k, v in new.to_dict().items():
            self.assertEqual(new.to_dict()[k], self.ins.to_dict()[k])
