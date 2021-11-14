#!/usr/bin/python3
"""This is the json serializer"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """serializes and deserializes an instance"""
    __file_path = "file.json"
    __objects = {}
    classes = {'BaseModel': BaseModel}


    def all(self):
        """Returns the dictionary @__objects"""
        return self.__class__.__objects

    def to_dict(self):
        """Return a dictionary of attributes using __dict__.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            Dictionary representation of all attributes of object
        """
        object_dict = {}
        object_dict.update(self.__dict__)
        object_dict.__setitem__('__class__', self.__class__.__name__)
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()

        return object_dict

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        fspath = obj.__class__.__name__
        self.__class__.__objects[obj] = "{}.{}".format(fspath, obj.id)

    def save(self):
        """serializes __objects to the json file"""
        with open(FileStorage.__file_path, "w") as t:
            for key, value in FileStorage.__objects.items:
                json.dump({key: value.to_dict()}, t)

    def reload(self):
        """deserializes the json file to __objects"""
        if not path.exists(FileStorage.__file_path):
            return None
        try:
            with open(self.__file_path, 'r') as fle:
                back = json.load(fle)
                for key in back.values():
                    cls = key["__class__"]
                    self.new(eval(cls)(**key))
        except Exception:
            pass
