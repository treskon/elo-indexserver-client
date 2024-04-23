import os

from eloclient.types import Unset

# This is your Test Root  /Users/...repos/elo-indexserver-client/test/
TEST_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def _check_not_unset(obj):
    assert type(obj) is not type(Unset)