#!/usr/bin/env python3
"""
Package initializer
"""
from models.base_model import BaseModel
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
