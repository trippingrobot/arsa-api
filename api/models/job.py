from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from api.models import meta

class JobModel(Model):
    """
    A DynamoDB Job
    """
    @meta.classwrapper
    class Meta(object):
        table_name = "job"

    name = UnicodeAttribute(hash_key=True)
