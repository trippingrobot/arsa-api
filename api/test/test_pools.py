from __future__ import print_function
import pytest # pylint: disable=unused-import

import api.pools as Pool
from api.models.pool import PoolModel

@pytest.fixture(scope='function')
def db_setup(request):
    """ setup database """
    pool = PoolModel(pool_id="1", account_id="1a", name="Foo")
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
