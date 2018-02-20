from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from api.models import util

class JobModel(Model):
    """
    A DynamoDB Job
    """
    @util.meta_classwrapper
    class Meta(object):
        table_name = "job"

    name = UnicodeAttribute(hash_key=True)
