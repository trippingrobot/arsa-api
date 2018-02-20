from __future__ import print_function
import pytest # pylint: disable=unused-import

from api.models.pool import PoolModel

def test_readonly_attrs():
    pool = PoolModel(pool_id="1", account_id="1a", name="Foo")

    new_values = {'account_id':'1b', 'name':'Bar'}
    pool.update(actions=PoolModel.mutable_actions(new_values))

    assert pool.account_id == '1a'
    assert pool.name == 'Bar'
