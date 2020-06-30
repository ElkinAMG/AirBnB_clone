"""
This module has Unittest for `FileStorage`.
"""

from models import storage
from models.user import User
from models.base_model import BaseModel
import unittest
import json
import os


class TestStorage(unittest.TestCase):
    """
    Testing Class for `FileStorage`.
    """

    def setUp(self):
        """
        Setting Up Needed For Testing.
        """

        self.n_user = User()
        self.dic = storage.all()
        self.another_user = None
        storage.save()

    def test_doc(self):
        """
        Test Complete Documentation Of Methods.
        """

        self.assertTrue(len(storage.__doc__) > 0)

        for p, item in enumerate(dir(storage)):
            if not item.startswith("_"):
                self.assertTrue(len(storage.__doc__[p]) > 0)

    def test_existence(self):
        """
        Checks if methods from Storage Engine works.
        """

        self.dic = storage.all()

        self.assertTrue(len(self.dic) > 0)

    def test_increment(self):
        """
        Checks if methods from Storage Engine works.
        """

        self.another_user = User()

        self.assertFalse(len(self.dic) != len(storage.all()))

    def test_existence_user(self):
        """
        Checks if methods from Storage Engine works.
        """

        self.another_user = User()

        iden = (self.another_user.__class__.__name__ +
                "." + self.another_user.id)

        self.assertTrue(iden in storage.all())

    def test_file_existence(self):
        """
        Checks if methods from Storage Engine works.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_check_json_loading(self):
        """
        Checks if methods from Storage Engine works.
        """

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def test_correct_instance(self):
        """
        Checks if methods from Storage Engine works.
        """

        with open("file.json") as f:
            dic = json.load(f)

            for k, v in dic.items():
                t_user = User(**v)
                self.assertEqual(issubclass(type(t_user), BaseModel), True)


if __name__ == "__main__":
    unittest.main()
    os.remove("file.json")
