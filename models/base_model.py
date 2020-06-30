#!/usr/bin/python3
"""base model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """base class for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Object instantiation for class
        """

        if len(kwargs) > 0:
                for k, v in kwargs.items():
                    if k != '__class__':
                        setattr(self, k, v)
                    if k == 'updated_at' or k == 'created_at':
                        dt = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, k, dt)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        returns a string represntation of the class name, id and dict
        """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates `updated_at` with the current datetime.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all from `instance`:
        """

        new_dic = self.__dict__.copy()
        new_dic["__class__"] = self.__class__.__name__
        for k, v in new_dic.items():
            if k == "created_at" or k == "updated_at":
                new_dic[k] = v.isoformat()
        return (new_dic)
