#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
import uuid
import datetime


class BaseModel:
    """
    Defines the BaseModel class.

    Attributes:
        id: The BaseModel id.
        created_id: The datetime at creation.
        updated_id: The datetime of last update.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            now = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)

    def __str__(self):
        class_name = type(self).__name__
        return f'[{class_name}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        result_dict = self.__dict__
        result_dict['__class__'] = type(self).__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
