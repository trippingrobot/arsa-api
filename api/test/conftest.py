from __future__ import print_function
import pytest
import os

from api.models.pool import PoolModel
from api.models.job import JobModel

MODELS = [PoolModel, JobModel]

@pytest.fixture(scope="session", autouse=True)
def setup_dynamo(request):
    os.environ["PYTHONENV"] = "test"
    create_tables()
    request.addfinalizer(delete_tables)

def create_tables():
    for model in MODELS:
        if not model.exists():
            model.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    print("Created tables")

def delete_tables():
    for model in MODELS:
        model.delete_table()
    print("Deleted tables")
