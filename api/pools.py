""" Pools Service """
from api.router import Router

@Router.route("pools.list")
def list_pools():
    """ List the available pools """
    pass

@Router.route("pools.get")
def get_pool(pool_id):
    """ Get pool by pool_id """
    return pool_id
