#!/usr/bin/python3
"""This is the json serializer"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes and deserializes an instance"""
    __file_path = "file.json"
    __objects = {}
    classes = {'BaseModel': BaseModel,
               'User': User,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Place': Place,
               'Review': Review}

    def all(self):
        """Returns the dictionary @__objects"""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        fspath = obj.__class__.__name__
        self.__class__.__objects[obj] = "{}.{}".format(fspath, obj.id)

    def save(self):
        """serializes __objects to the json file"""
        to_move = {}
        for ob, le in FileStorage.__objects.items():
            to_move[ob] = le.to_dict()
        with open(FileStorage.__file_path, "w") as fle:
            json.dump(to_move, fle)

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
