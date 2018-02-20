""" Pools Service """
from api.router import Router

from api.models.pool import PoolModel

@Router.route("pools.list")
def list_pools(account_id):
    """ List the available pools """
    return list(PoolModel.query(account_id))

@Router.route("pools.get")
def get_pool(account_id, pool_id):
    """ Get pool by pool_id """
    return PoolModel.get(account_id, pool_id)

@Router.route("pools.update")
def update_pool(account_id, pool_id, **kwargs):
    """ Update pool by pool_id """
    pool = PoolModel.get(account_id, pool_id)

    # update data pool by sending only mutable actions, ingoring immutable attributes
    pool.update(actions=PoolModel.mutable_actions(kwargs))

    return pool
