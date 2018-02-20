import os

def meta_classwrapper(cls):
    """ A class decorator to add environment specific attributes
        to a pynamodb Meta class.
    """
    env = os.getenv('PYTHONENV', 'dev')
    setattr(cls, "table_name", "arsa-%s-%s" % (env, cls.table_name))

    if env == "dev":
        setattr(cls, "host", "http://localhost:8000")

    return cls


class Immutable(object):
    """docstring for Sanitize."""
    immutable_attributes = []

    def is_immutable(self, attribute):
        return attribute in self.immutable_attributes

    def sanitize_attributes(self, attributes):
        for attr in self.immutable_attributes:
            if attr in attributes:
                attributes.pop(attr)
        return attributes
