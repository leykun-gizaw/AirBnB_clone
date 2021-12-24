#!/usr/bin/python3
"""Unit tests for `file_storage` module"""
import os
import json
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class to test class FileStorage."""

    def setUp(self):
        """Fixtures setup method.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]
        return None

    def tearDown(self):
        """Fixtures teardown method.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        try:
            os.remove(storage._FileStorage__file_path)
        except Exception:
            pass
        return None

    def test_private_attributes(self):
        """Test if attributes that are supposed to be private are private.

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

        1.  Check if returned value is a dictionary
        2.  Check if initially __objects is an empty dictionary
        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(len(storage.all()), 0)

        return None

    def test_new(self):
        """Test if `new` method creates according to a format.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        test_object = BaseModel()
        storage.new(test_object)

        with self.assertRaises(TypeError):
            storage.new()

        storage.new(test_object)

        for k, v in storage._FileStorage__objects.items():
            self.assertIsInstance(v, BaseModel)

            id_regex = storage._FileStorage__objects[k].to_dict()["id"]
            cls_regex = storage._FileStorage__objects[k].to_dict()["__class__"]

            key = cls_regex + '.' + id_regex
            self.assertEqual(k, key)
        return None

    def test_save(self):
        """Test if `save` method serializes `__objects` to `__file_path`.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        test_object = BaseModel()
        storage.save()
        key = test_object.to_dict()["__class__"] + "." + test_object.id
        with open(storage._FileStorage__file_path, 'r') as file:
            obj = json.load(file)

        self.assertEqual(test_object.to_dict(), obj[key])
        self.assertNotEqual(os.path.getsize("file.json"), 0)
        self.assertTrue(os.path.exists("file.json"))
        return None

    def test_reload(self):
        """Test if `reload` method Deserialzes `__file_path`.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        test_object = BaseModel()
        storage.save()
        storage.reload()
        key = test_object.to_dict()["__class__"] + "." + test_object.id
        self.assertEqual(storage._FileStorage__objects[key].to_dict(),
                         test_object.to_dict())
        return None

    def test_reload_no_file_json(self):
        """Test reload for non existent file.

        Args:
            self (object): type(self) = <class '__main__.TestFileStorage'>

        Returns:
            None
        """
        self.assertEqual(storage.reload(), None)
        return None
