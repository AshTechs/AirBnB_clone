#!/usr/bin/python3
"""Write a class FileStorage that serializes instances to
a JSON file and deserializes JSON file to instances.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_dict = obj.to_dict()
        name = f"{obj_dict['__class__']}.{obj.id}"
        FileStorage.__objects[name] = obj

    def save(self):
        """

        """
        all_objects = FileStorage.__objects
        dict_object = {}

        for obj in all_objects.keys():
            dict_object[obj] = all_objects[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as fd:
            json.dump(dict_object, fd)

    def reload(self):
        """_summary_
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
                try:
                    obj_dict = json.load(fd)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")

                        m_cls = eval(class_name)
                        instance = m_cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
