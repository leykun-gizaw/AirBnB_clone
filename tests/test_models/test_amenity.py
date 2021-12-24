#!/usr/bin/python3
"""Unit tests for `amenity.py` module."""
from unittest import TestCase
from models.amenity import Amenity


class TestUser(TestCase):
    """Class of `Amenity` class test methods."""

    def test_name(self):
        """Test for `name` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_amenity = Amenity()

        self.assertIsInstance(test_amenity.name, str)
        return None
