import pytest
from downloader import downloader
from ioer import ioer


@pytest.fixture
def downloader_test():
    return downloader()


@pytest.fixture
def ioer_test():
    return ioer()

def test_ioer_get_config(ioer_test):
    ioer_test.reset_config()
    assert ioer_test.get_config() == ioer_test.default_config
    ioer_test.update_config({"qn": 120})
    assert ioer_test.get_config()["qn"] == 120
    ioer_test.reset_config()

def test_ioer_reset_config(ioer_test):
    ioer_test.reset_config()
    assert ioer_test.read() == ioer_test.default_config

def test_ioer_update_config(ioer_test):
    ioer_test.update_config({"dm": True})
    assert ioer_test.read()["dm"] == True
    ioer_test.reset_config()



if __name__ == "__main__":
    pytest.main(["tester.py"])
