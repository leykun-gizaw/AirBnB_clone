#!/usr/bin/python3
"""Unit tests for `place.py` module."""
from unittest import TestCase
from models.place import Place


class TestUser(TestCase):
    """Class of `Place` class test methods."""

    def test_city_id(self):
        """Test for `city_id` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.city_id, str)
        return None

    def test_user_id(self):
        """Test for `user_id` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.user_id, str)
        return None

    def test_name(self):
        """Test for `name` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.name, str)
        return None

    def test_description(self):
        """Test for `description` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.description, str)
        return None

    def test_number_rooms(self):
        """Test for `number_rooms` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.number_rooms, int)
        return None

    def test_number_bathrooms(self):
        """Test for `number_bathrooms` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.number_bathrooms, int)
        return None


    def test_max_guest(self):
        """Test for `max_guest` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.max_guest, int)
        return None

    def test_price_by_night(self):
        """Test for `price_by_night` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.price_by_night, int)
        return None

    def test_latitude(self):
        """Test for `latitude` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.latitude, float)
        return None

    def test_longitude(self):
        """Test for `longitude` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.longitude, float)
        return None

    def test_amenity_ids(self):
        """Test for `amenity_ids` class attribute.

        Args:
            self (object): Refers to current object.

        Returns:
            None
        """
        test_place = Place()

        self.assertIsInstance(test_place.amenity_ids, list)
        return None
