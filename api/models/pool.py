from datetime import datetime

from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, UTCDateTimeAttribute)

from api.models.util import (meta_classwrapper, generate_uuid)
from api.models.attributes import (Immutable, TaxonomyAttribute)

class PoolModel(Model, Immutable):
    """
    A DynamoDB DataPool
    """
    @meta_classwrapper
    class Meta(object):
        table_name = "pool"

    account_id = UnicodeAttribute(hash_key=True) # Partiton by account for flexible lookups
    pool_id = UnicodeAttribute(range_key=True, default=generate_uuid()) # sort by unique pool ids
    created_at = UTCDateTimeAttribute(default=datetime.now())
    name = UnicodeAttribute()
    taxonomy = TaxonomyAttribute()

    # Cannot be updated.
    immutable_attributes = ["account_id", "pool_id", "created_at"]
