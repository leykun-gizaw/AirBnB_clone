#!/usr/bin/python3
"""This is the json serializer"""
import json
from os import path
from models.base_model import BaseModel

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        fspath = obj.__class__.__name__
        self.__class__.__objects[obj] = "{}.{}".format(fspath, obj.id)

    def save(self):
        """serializes __objects to the json file"""
        obdict = FileStorage.__objects
        dicts = {obj: obdict[obj].to_dict() for obj in obdict.keys()}
        with open(FileStorage.__file_path, "w") as fle:
            json.dump(dicts, fle)

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
