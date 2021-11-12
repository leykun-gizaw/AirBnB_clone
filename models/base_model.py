#!/usr/bin/python3
"""Module defines BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all other classes."""

    def __init__(self, *args, **kwargs):
        """Instance initializer.

        Args:
            self (object): Refers to instantiated object.
            args (parameter): Non keyword arguments
            kwargs (parameter): keyword arguments

        Returns:
            None
        """
        self.format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
        else:
            for key in kwargs.keys():
                if key == 'created_at' or key == 'updated_at':
                    kwargs[key] = datetime.strptime(kwargs[key], self.format)
                    setattr(self, key, kwargs[key])
                elif key != '__class__':
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Return string representation of object.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            String representation of the object that called it.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update attribute 'updated_at' with current time.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            None
        """
        self.updated_at = datetime.datetime.now().isoformat()
        return None

    def to_dict(self):
        """Return a dictionary of attributes using __dict__.

        Args:
            self (object): Refers to instantiated object.

        Returns:
            Dictionary representation of all attributes of object
        """
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
