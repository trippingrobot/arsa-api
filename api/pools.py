""" Pools Service """
import boto3

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

@Router.route("pools.drop")
def drop_pool(account_id, pool_id):
    """ Get pool by pool_id """
    PoolModel.get(account_id, pool_id).delete()

@Router.route("pools.create")
def create_pool(account_id, **kwargs):
    """ Create a data pool with account id """
    sanitized = PoolModel.sanitize_immutable_attrs(kwargs)
    pool = PoolModel(account_id=account_id, **sanitized)

    # Pool must be saved before Athena table can be created
    pool.save()

    client = boto3.client('athena')
    client.start_query_execution(QueryStrin='CREATE')
    # TODO: Create Athena table with namespace "env.account_id.pool_id"

    return pool
