#!/usr/bin/python3
"""file storage"""
import json


class FileStorage:
    """
    class for storing files
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in `__objects` the obj with key `<obj class name>.id`
        """

        if obj:
            self.key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[self.key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        n_dic = self.__objects.copy()

        for k, v in n_dic.items():
            n_dic[k] = v.to_dict().copy()

        with open(self.__file_path, "w+", encoding="utf-8") as file:
            json.dump(n_dic,
                      file, indent=4, sort_keys=True)

    def reload(self):
        """
        deserializes the JSON file to `__objects`
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as file:
                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.amenity import Amenity
                from models.state import State
                from models.review import Review
                from models.place import Place

                stamp = json.load(file)
                for k, v in stamp.items():
                    self.__objects[k] = eval("{}(**v)".format(
                        k.split(".")[0]))
        except:
            pass
