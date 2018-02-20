from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from api.models.util import (meta_classwrapper, Immutable)

class PoolModel(Model, Immutable):
    """
    A DynamoDB DataPool
    """
    @meta_classwrapper
    class Meta(object):
        table_name = "pool"

    account_id = UnicodeAttribute(hash_key=True) # Partiton by account for flexible lookups
    pool_id = UnicodeAttribute(range_key=True) # sort by unique pool ids
    name = UnicodeAttribute()

    # Cannot be updated.
    immutable_attributes = ["account_id", "pool_id"]
