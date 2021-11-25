#!/usr/bin/python3
"""Unit tests for 'base_model.py' module."""
import os
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test class BaseModel."""

    test_object = BaseModel()

    def test__init__(self):
        """Test BaseModel initial instance attributes.

        1.  Check existence of attributes.
        2.  Check type of attributes.
        3.  Check if 'created_at' & 'updated_at' are identical.

        Args:
            self (object): Refers to current object.

        Returns:
            None.
        """
        # Check No_ 1. Check existence of attributes
        self.assertIn("id", self.test_object.__dict__)
        self.assertIn("created_at", self.test_object.__dict__)
        self.assertIn("updated_at", self.test_object.__dict__)

        # Check No_ 2. Check type of attributes
        self.assertIsInstance(self.test_object.id, str)
        self.assertIsInstance(uuid.UUID(self.test_object.id), uuid.UUID)
        self.assertIsInstance(self.test_object.created_at, datetime)
        self.assertIsInstance(self.test_object.updated_at, datetime)

        # Check No_ 3. Check identical 'created_at' & 'updated_at'
        self.assertEqual(self.test_object.created_at,
                         self.test_object.updated_at)
        return None

    def test__str__(self):
        """Test string representation of instances of BaseModel.


        Check the output of __str__ with a regular expression.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        regex = r'\[' + self.test_object.__class__.__name__ + r'\]' +\
            r' \(.{8}-.{4}-.{4}-.{4}-.{12}\) \{.+\}'
        self.assertRegex(self.test_object.__str__(), regex)
        return None

    def test_save(self):
        """Test save method for updated time of last modification.

        Check if save method actually saves the `updated_at` attribute to be
        later than `created_at` after a given amount of time.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        local_Test_Object = BaseModel()
        create_time = local_Test_Object.created_at
        local_Test_Object.save()
        update_time = local_Test_Object.updated_at
        self.assertGreater(update_time, create_time)
        os.remove("file.json")
        return None

    def test_to_dict(self):
        """Test `to_dict` method for valid attributes dictionary.

        1.  Check if return value is of dictionary type.
        2.  Check if all keys in returned dictionary are in __dict__.
        3.  Check if `created_at` & `updated_at` are string types.
        4.  Check if `__class__` key is present with correct value.
        5.  Check string format datetimes are in correct format.
        6.  Check when provided a dict to its object, it returns that same dict
        with additional `__class__` attribute already set.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        # Check No_ 1:
        self.assertIsInstance(self.test_object.to_dict(), dict)

        # Check No_ 2:
        for k, *_ in self.test_object.to_dict().items():
            if k != "__class__":
                self.assertIn(k, self.test_object.__dict__)

        # Check No_ 3:
        self.assertIsInstance(self.test_object.to_dict()["created_at"], str)
        self.assertIsInstance(self.test_object.to_dict()["updated_at"], str)

        # Check No_4:
        self.assertIn("__class__", list(self.test_object.to_dict().keys()))

        # Check No_5:
        create_str = self.test_object.to_dict()["created_at"]
        update_str = self.test_object.to_dict()["created_at"]
        format = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(create_str, format)
        except Exception:
            self.assertTrue(False, msg="`created_at` is in incorect format")
        try:
            datetime.strptime(update_str, format)
        except Exception:
            self.assertTrue(False, msg="`updated_at` is in incorect format")

        # Check No_ 6:
        dictionary = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": datetime.now().isoformat(),
            "name": "My_First_Model"
        }
        local_Test_Object = BaseModel(**dictionary)
        self.assertTrue(dictionary == local_Test_Object.to_dict())

        return None
