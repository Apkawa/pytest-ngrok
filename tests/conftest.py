import pytest


@pytest.fixture(scope='session')
def ngrok_bin():
    return '/tmp/bin/ngrok'
