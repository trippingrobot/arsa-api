from __future__ import print_function
import pytest # pylint: disable=unused-import

import api.pools as Pool
from api.models.pool import PoolModel
from api.models.attributes import (FieldAttribute, TaxonomyAttribute)

from .mocks.athena import mock_athena
from moto import mock_dynamodb2

@pytest.fixture(scope='function')
def db_setup(request):
    """ setup database """
    fields = [FieldAttribute(name='last_name', field_type='int')]
    taxonomy = TaxonomyAttribute(format_type="csv", fields=fields)

    pool = PoolModel(pool_id="1", account_id="1a", name="Foo", taxonomy=taxonomy)
    pool.save()
    request.addfinalizer(pool.delete)

@pytest.mark.usefixtures("db_setup")
def test_list_pools():
    """ list pools by account id. """
    pools = Pool.list_pools("1a")
    assert isinstance(pools, list)
    assert len(pools) == 1
    assert pools[0].name == "Foo"

@pytest.mark.usefixtures("db_setup")
def test_get_pool():
    """ get pool by accounnt id and pool_id """
    pool = Pool.get_pool("1a", "1")
    assert pool.name == "Foo"

@pytest.mark.usefixtures("db_setup")
def test_update_pool():
    """ get pool by accounnt id and pool_id """
    pool = Pool.update_pool(**{"account_id":"1a", "pool_id":"1", "name":"Bar"})
    assert pool.name == "Bar"

@pytest.mark.usefixtures("db_setup")
def test_delete_pool():
    """ drop pool by accounnt id and pool_id """
    Pool.drop_pool("1a", "1")

    with pytest.raises(Exception):
        Pool.get_pool("1a", "1")

@mock_athena
@mock_dynamodb2
def test_create_pool():
    """ create pool by accounnt id and name"""
    req = {
        "name": "Foo",
        "taxonomy": {
            "format_type": "csv",
            "fields": [
                {
                    "name": "first_name",
                    "field_type": "int"
                }
            ]
        }
    }

    pool = Pool.create_pool("1a", **req)

    # Make sure the object exists on the database
    PoolModel.get(pool.account_id, pool.pool_id)

    assert pool.account_id == "1a"
    assert pool.pool_id
    assert pool.name == "Foo"
