#!/usr/bin/python3
"""Unit tests for `file_storage` module"""
import os
import json
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class to test class FileStorage."""

    def test_private_attributes(self):
        """Test if attributes that are suppsed to be private are private.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        with self.assertRaises(AttributeError):
            storage.__file_path
        with self.assertRaises(AttributeError):
            storage.__objects
        return None

    def test_all(self):
        """Test the return value of `all` method.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        self.assertIsInstance(storage.all(), dict)
        return None

    def test_new(self):
        """Test if `new` method creates according to a format.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        for k, v in storage._FileStorage__objects.items():
            self.assertIsInstance(v, BaseModel)

            id_regex = storage._FileStorage__objects[k].to_dict()["id"]
            cls_regex = storage._FileStorage__objects[k].to_dict()["__class__"]

            self.assertRegex(k, id_regex)
            self.assertRegex(k, cls_regex)
        return None

    def test_save(self):
        """Test if `save` method serializes `__objects` to `__file_path`.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        test_obj1 = BaseModel()
        test_obj1.save()

        key = test_obj1.to_dict()["__class__"] + "." + test_obj1.id

        with open("file.json", "r") as file:
            obj = json.load(file)

        os.remove("file.json")

        self.assertEqual(test_obj1.to_dict(), obj[key])
        return None

    def test_reload(self):
        """Test if `reload` method Deserialzes `__file_path`.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        test_obj = BaseModel()
        test_obj.save()

        storage.reload()
        key = test_obj.to_dict()["__class__"] + "." + test_obj.id

        with open("file.json", "r") as file:
            obj = json.load(file)

        os.remove("file.json")

        self.assertEqual(storage._FileStorage__objects[key].to_dict(),
                         test_obj.to_dict())
        return None
