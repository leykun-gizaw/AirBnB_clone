#!/usr/bin/python3
"""Module defines `FileStorage` class."""
import json


class FileStorage:
    """Serialize to a JSON file and deserialize JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary `__objects`.

        Args:
            self (object): <class '__main__.FileStorage'> instance

        Returns:
            __objects
        """
        return self.__class__.__objects

    def new(self, obj):
        """Populates `__objects`.

        __objects will be populated with a key of `<obj's class name>.id`
        format and a value of that key will be obj itself.

        Args:
            self (object): <class '__main__.FileStorage'> instance
            obj (obj): Instance of class `obj.__class__`.

        Returns:
            None
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        return None

    def save(self):
        """Serialize `__objects` to `__file_path`.

        Args:
            self (object): <class '__main__.FileStorage'> instance

        Returns:
            None
        """
        serialize_me_dict = {}
        for key in self.__objects.keys():
            serialize_me_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialize_me_dict, file)
        return None

    def reload(self):
        """Deserialize from `__file_path` to `__objects`

        Args:
            self (object): <class '__main__.FileStorage'> instance

        Returns:
            None
        """
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import BaseModel

        classes_dict = {
            "User": User,
            "City": City,
            "Place": Place,
            "State": State,
            "Review": Review,
            "Amenity": Amenity,
            "BaseModel": BaseModel,
        }
        from models.user import User
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as file:
                deserialize_me = json.load(file)
            for k, v in deserialize_me.items():
                self.__objects[k] = classes_dict[v["__class__"]](**v)
        except Exception:
            pass
