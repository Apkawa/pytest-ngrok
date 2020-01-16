import distutils.spawn
import os
from pathlib import Path

from pytest import fixture

from pytest_ngrok.install import install_bin
from pytest_ngrok.manager import NgrokContextManager


def pytest_addoption(parser):
    parser.addoption(
        '--ngrok',
        default=distutils.spawn.find_executable('ngrok'),
        help='path to ngrok [%default]'
    )


REMOTE_URL = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'


@fixture(scope='function')
def ngrok_install_url():
    # TODO verify
    return REMOTE_URL


@fixture(scope='function')
def ngrok_bin(request, ngrok_install_url):
    # TODO get from setup.cfg
    ngrok_path = request.config.getoption('--ngrok', '/usr/local/bin/ngrok')
    if not ngrok_path:
        ngrok_path = os.path.join(Path.home(), '.local', 'bin', 'ngrok')
    if not os.path.exists(ngrok_path):
        install_bin(ngrok_path, remote_url=ngrok_install_url)
    return ngrok_path


@fixture(scope='function')
def ngrok(ngrok_bin):
    managers = []

    def _wrap(port=None):
        manager = NgrokContextManager(ngrok_bin, port)
        managers.append(manager)
        return manager()

    yield _wrap

    for m in managers:
        m.stop()
