#!/usr/bin/python3
"""Module defines BaseModel class."""
from uuid import uuid4
from copy import deepcopy
from models import storage
from datetime import datetime


class BaseModel:
    """BaseModel class to create instances."""

    def __init__(self, *_, **kwargs):
        """Initialize BaseModel instances.

        Args:
            self (object): <class '__main__.BaseModel'> type object.
            kwargs (parameter): keyworded arguments

        Returns:
            None
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = deepcopy(self.created_at)
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, format))
                    else:
                        setattr(self, k, v)
        return None

    def __str__(self):
        """Return string representation of current object.

        Args:
            self (object): <class '__main__.BaseModel'> type object.

        Returns:
            String representation of the object that called it.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Update 'updated_at' attrib with current time stamp.

        Args:
            self (object): <class '__main__.BaseModel'> type object.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
        return None

    def to_dict(self):
        """Return a dictionary of attributes using __dict__.

        Args:
            self (object): <class '__main__.BaseModel'> type object.

        Returns:
            Dictionary representation of all attributes of object
        """
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
    pass
