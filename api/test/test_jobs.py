from __future__ import print_function
import pytest

import api.jobs as Jobs
from api.models.job import JobModel

@pytest.fixture(scope='module')
def db_setup():
    job = JobModel("John")
    job.save()
    return job

@pytest.mark.usefixtures("db_setup")
def test_get_job():
    job = Jobs.get_job("John")
    assert job.name == "John"
