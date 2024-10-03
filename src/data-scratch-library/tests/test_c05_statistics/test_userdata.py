from os import remove
from os.path import exists, dirname, abspath

import pytest

from dsl.c05_statistics.c01_userdata import UserData


@pytest.fixture(name="ud01")
def user_data_fixture():
    """Fixture to provide a sample UserData instance."""
    return UserData(
        daily_minutes=[1, 68.77, 51.25, 52.08, 38.36],
        num_friends=[100, 49, 41, 40, 25]
    )


def test_to_json(ud01):
    """Test the to_json method."""
    ouput_path = "example_user_data.out.json"
    ud01.to_json(ouput_path)
    assert exists(ouput_path)
    data = UserData.from_json(ouput_path)
    assert len(data.daily_minutes) == 5
    assert len(data.num_friends) == 5
    remove(ouput_path)


def test_from_json(ud01):
    """Test the from_json method."""
    path_to_example=abspath(f"{dirname(__file__)}/../../../../data/example_user_data.json")
    loaded_user_data = UserData.from_json(path_to_example)
    assert len(loaded_user_data.daily_minutes) == 5
    assert len(loaded_user_data.num_friends) == 5
