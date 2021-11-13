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

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        fspath = obj.__class__.__name__
        self.__class__.__objects[obj] = "{}.{}".format(fspath, obj.id)

    def save(self):
        """serializes __objects to the json file"""
        with open(FileStorage.__file_path, "r+") as t:
            json.dump(FileStorage.__objects, t)

    def reload(self):
        """deserializes the json file to __objects"""
        if not path.exists(FileStorage.__file_path):
            return None
        else:
            with open(self.__class__.__file_path, "r") as fle:
                to_dict = json.loads(fle.read())
            for key in to_dict.keys():
                for cls in FileStorage.classes.keys():
                    if cls in key:
                        FileStorage.__objects[key] = FileStorage.classes[cls\
                        ](**(to_dict[key]))
