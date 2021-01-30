import pytest
import random


@pytest.fixture
def mon_keyring():
    def make_keyring(default=False):
        if default:
            key = "AQBvaBFZAAAAABAA9VHgwCg3rWn8MaX8KL01A=="
        else:
            key = "%032x==" % random.getrandbits(128)

        return """
        [mon.]
            key = %s
                caps mon = "allow *
            """ % key
    return make_keyring


def test_default_key(mon_keyring):
    contents = mon_keyring(default=True)
    assert "AQBvaBFZAAAAABAA9VHgwCg3rWn8MaX8KL01A==" in contents
