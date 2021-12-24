#!/usr/bin/python3
"""Unit tests for `amenity.py` module."""
from unittest import TestCase
from models.review import Review


class TestUser(TestCase):
    """Class of `Review` class test methods."""

    def test_place_id(self):
        """Test for `place_id` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_review = Review()

        self.assertIsInstance(test_review.place_id, str)
        return None

    def test_user_id(self):
        """Test for `user_id` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_review = Review()

        self.assertIsInstance(test_review.user_id, str)
        return None

    def test_text(self):
        """Test for `text` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_review = Review()

        self.assertIsInstance(test_review.text, str)
        return None
