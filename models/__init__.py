#!/usr/bin/python3
"""__init__ module used to initialize a package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
