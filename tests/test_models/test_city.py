#!/usr/bin/python3
"""Unit tests for `city.py` module."""
from unittest import TestCase
from models.city import City


class TestUser(TestCase):
    """Class of `City` class test methods."""

    def test_state_id(self):
        """Test for `state_id` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_city = City()
        self.assertIsInstance(test_city.state_id, str)
        return None

    def test_name(self):
        """Test for `name` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_city = City()

        self.assertIsInstance(test_city.name, str)
        return None
