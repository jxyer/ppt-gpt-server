import json


class BaseEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
