import os

from eloclient.types import Unset

TEST_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

def _check_not_unset(obj):
    assert type(obj) is not type(Unset)