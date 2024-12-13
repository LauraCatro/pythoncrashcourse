import pytest
from pathlib import Path

@pytest.fixture
def path():
    path = Path('python_work/Files/guest.txt')
    return path

def test_name_in_guest(path):
    assert path.open().read() == 'Diana'
    

