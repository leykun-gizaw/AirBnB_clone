#!/usr/bin/python3
"""Unit tests for 'base_model.py' module."""
from time import sleep
import sys
import unittest
from datetime import datetime
from models.base_model import BaseModel

sys.path.append("../../")


class TestBaseModel(unittest.TestCase):
    """Class to test class BaseModel."""

    test_object = BaseModel()

    def test___init__(self):
        """Test BaseModel initial instance attribute types.

        Check type of the attributes BaseModel's objects have.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            None
        """
        self.assertTrue(isinstance(self.test_object.id,
                                   str))
        self.assertTrue(isinstance(self.test_object.created_at,
                                   datetime))
        self.assertTrue(isinstance(self.test_object.updated_at,
                                   datetime))
        return None

    def test_save(self):
        """Test BaseModel's 'save' public instance method.

        Check the time-stamp of an object after its instantiation.
        Initial time-stamp must be less compared to the time-stamp after we run
        the save method on it.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            None
         initial = self.test_object.created_at.timestamp()
         self.test_object.save()
         after_save = self.test_object.updated_at.timestamp()

         self.assertTrue(after_save > initial)
         return None
        """
    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        """testing two saves"""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        """testing arguments behaviour"""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        """testing if is updated"""
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_to_dict(self):
        """Test BaseModel's 'to_dict' public instance method.

        1. Check the return value of 'to_dict' method is a dictionary object.
        2. Check if '__class__' key is present in the list of keys
        3. Check if 'created_at' & 'updated_at' keys from returned dictionary
           are of string type.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            None
        """
        # Check No_ 1. Check type of method's return value
        self.assertTrue(isinstance(self.test_object.to_dict(), dict))

        # Check No_ 2. Check if '__class__' key is present in the list of keys
        self.assertIn("__class__", list(self.test_object.to_dict().keys()))

        # Check No_ 3. Check if 'created_at' & 'updated_at' are strings
        self.assertIsInstance(self.test_object.to_dict()["created_at"], str)
        self.assertIsInstance(self.test_object.to_dict()["updated_at"], str)
    pass


if __name__ == "__main__":
    unittest.main()
