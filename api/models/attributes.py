""" Custom Attributes """
from pynamodb.attributes import (MapAttribute, ListAttribute, UnicodeAttribute)

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

    @classmethod
    def sanitize_immutable_attrs(cls, attributes):
        """ return dict of sanitized attributes removing immutable ones """
        return {k:v for k, v in attributes.items() if cls.is_immutable(k) is False}

class FieldAttribute(MapAttribute):
    """ Field embedded map attribute """
    name = UnicodeAttribute()
    field_type = UnicodeAttribute()

class TaxonomyAttribute(MapAttribute):
    """ Taxonomy embedded map attribute """
    format_type = UnicodeAttribute()
    fields = ListAttribute(of=FieldAttribute)
