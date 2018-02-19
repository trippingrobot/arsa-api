from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from api.models import meta

class PoolModel(Model):
    """
    A DynamoDB DataPool
    """
    @meta.classwrapper
    class Meta(object):
        table_name = "pool"

    name = UnicodeAttribute(hash_key=True)
