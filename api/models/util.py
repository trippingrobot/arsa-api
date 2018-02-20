""" Model Utility package """
import os
import uuid

def generate_uuid():
    """ Generate a UUID value """
    return uuid.uuid4().hex

def meta_classwrapper(cls):
    """ A class decorator to add environment specific attributes
        to a pynamodb Meta class.
    """
    env = os.getenv('PYTHONENV', 'dev')
    setattr(cls, "table_name", "arsa-%s-%s" % (env, cls.table_name))

    if env == "dev":
        setattr(cls, "host", "http://localhost:8000")

    return cls
