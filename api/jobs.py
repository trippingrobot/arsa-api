""" Jobs Service """
from api.router import Router
from api.models.job import JobModel

@Router.route("jobs.get")
def get_job(job_id):
    """ Get pool by job_id """
    return JobModel.get(job_id)
