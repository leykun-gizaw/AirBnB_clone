#!/usr/bin/python3
"""Unit tests for `user.py` module."""
from unittest import TestCase
from models.user import User


class TestUser(TestCase):
    """Class of `User` class test methods."""

    def test_email(self):
        """Test for `email` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_user = User()

        self.assertIsInstance(test_user.email, str)
        return None

    def test_password(self):
        """Test for `password` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_user = User()

        self.assertIsInstance(test_user.password, str)
        return None

    def test_first_name(self):
        """Test for `first_name` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_user = User()

        self.assertIsInstance(test_user.first_name, str)
        return None

    def test_last_name(self):
        """Test for `last_name` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_user = User()

        self.assertIsInstance(test_user.last_name, str)
        return None
