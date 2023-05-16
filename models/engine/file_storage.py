import json
import os


class FileStorage:
    """
      Serializes instances to a JSON file and deserializes JSON file to instances:
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        # Check if the JSON file exists
        if os.path.exists(self.__file_path):
            # Open the JSON file for reading
            with open("file.json", "r") as f:
                self.__objects = json.load(f)
