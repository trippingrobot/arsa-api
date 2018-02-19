import os

def classwrapper(cls):
    """ A class decorator to add environment specific attributes
        to a pynamodb Meta class.
    """
    env = os.getenv('PYTHONENV', 'dev')
    setattr(cls, "table_name", "arsa-%s-%s" % (env, cls.table_name))

    if env == "dev":
        setattr(cls, "host", "http://localhost:8000")

    return cls
