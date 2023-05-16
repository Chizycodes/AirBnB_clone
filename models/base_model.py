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
    id = ''
    created_at = ''
    updated_at = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        now = datetime.datetime.utcnow()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop('_sa_instance_state', None)
        class_name = type(self).__name__
        return f'[{class_name}] ({self.id}) {d}'

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = str(type(self).__name__)
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        result_dict.pop('_sa_instance_state', None)
        return result_dict

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
