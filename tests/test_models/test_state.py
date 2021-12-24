#!/usr/bin/python3
"""Unit tests for `state.py` module."""
from unittest import TestCase
from models.state import State


class TestUser(TestCase):
    """Class of `State` class test methods."""

    def test_name(self):
        """Test for `name` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_state = State()

        self.assertIsInstance(test_state.name, str)
        return None
