#!/usr/bin/python3
"""Initializes the file storage for models directory"""
from models.engine.file_storage import FileStorage

# Initialize the FileStorage instance
storage = FileStorage()

# Reload data from file
storage.reload()

