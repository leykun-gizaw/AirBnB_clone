#!/usr/bin/python3
"""Unit tests for 'base_model.py' module."""
import sys
import unittest
from datetime import datetime

sys.path.append("../../")
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class to test class BaseModel."""

    test_object = BaseModel()

    def test_initial_attribute_types(self):
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

    def test_save_method(self):
        """Test BaseModel's 'save' public instance method.

        Check the time-stamp of an object after its instantiation.
        Initial time-stamp must be less compared to the time-stamp after we run
        the save method on it.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            None
        """
        initial = self.test_object.created_at.timestamp()
        self.test_object.save()
        after_save = self.test_object.updated_at.timestamp()

        self.assertTrue(after_save > initial)
        return None

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
