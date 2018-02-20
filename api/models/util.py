""" Model Utility package """
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
    """docstring for Immutable."""

    immutable_attributes = []

    @classmethod
    def is_immutable(cls, attribute):
        """ Return if attribute name is immutable """
        return attribute in cls.immutable_attributes

    @classmethod
    def mutable_actions(cls, attributes):
        """ return list of filtered update actions """
        update_actions = [getattr(cls, k).set(v)
                          for k, v in attributes.items()
                          if cls.is_immutable(k) is False]
        return update_actions
