import uuid
import datetime


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self):
        now = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now

    def __str__(self):
        class_name = type(self).__name__
        return f'[<{class_name}>] (<{self.id}>) <{self.__dict__}>'

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        result_dict = self.__dict__
        result_dict['__class__'] = type(self).__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
