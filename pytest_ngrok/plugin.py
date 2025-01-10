import distutils.spawn
import os
from pathlib import Path

from pytest import fixture

from pytest_ngrok.install import install_bin, get_bin_version
from pytest_ngrok.manager import NgrokContextManager

try:
    from .django import *  # noqa
except ImportError:
    pass


def pytest_addoption(parser):
    parser.addoption(
        "--ngrok-bin",
        default=distutils.spawn.find_executable("ngrok"),
        help="path to ngrok [%default]",
    )
    parser.addoption(
        "--ngrok-no-install",
        action="store_true",
        default=False,
        help="Disable fetch ngrok binary from remote",
    )

    parser.addoption(
        "--ngrok-force-install",
        action="store_true",
        default=False,
        help="Force fetch ngrok bin from remote",
    )


NGROK_VERSION = None
REMOTE_URL = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip"


@fixture(scope="session")
def ngrok_authtoken():
    return os.environ.get("NGROK_AUTHTOKEN")


@fixture(scope="session")
def ngrok_install_url():
    # TODO verify
    return REMOTE_URL


@fixture(scope="session")
def ngrok_version():
    # For pin version
    return NGROK_VERSION


@fixture(scope="session")
def ngrok_allow_install(request):
    """
    Allow install ngrok from remote. Default: True
    """
    return not request.config.getoption("--ngrok-no-install", False)


@fixture(scope="session")
def ngrok_bin(request):
    """
    Path to ngrok-bin. by default - $HOME/.local/bin/ngrok
    """
    ngrok_path = request.config.getoption("--ngrok-bin")
    if not ngrok_path:
        ngrok_path = os.path.join(Path.home(), ".local", "bin", "ngrok")
    return ngrok_path


@fixture(scope="session")
def _ngrok_bin(
    request, ngrok_bin, ngrok_install_url, ngrok_allow_install, ngrok_version
):
    need_install = False
    force_install = request.config.getoption("--ngrok-force-install")
    if force_install:
        need_install = True
    elif not os.path.exists(ngrok_bin):
        if not ngrok_allow_install:
            raise OSError("Ngrok %s bin not found!" % ngrok_bin)
        need_install = True
    else:
        version = get_bin_version(ngrok_bin)
        if ngrok_version and version != ngrok_version:
            if not ngrok_allow_install:
                raise OSError(
                    f"Ngrok {ngrok_bin} version mismatch!"
                    f" Need '{ngrok_version}', got '{version}'"
                )
            need_install = True

    if need_install:
        install_bin(ngrok_bin, remote_url=ngrok_install_url)
    yield ngrok_bin


@fixture(scope="function")
def ngrok(_ngrok_bin, ngrok_authtoken):
    """
    Usage:
    ```
    def test_ngrok_context_manager(ngrok, httpserver):
        httpserver.expect_request("/foobar").respond_with_data("ok")
        with ngrok(httpserver.port) as remote_url:
            assert 'ngrok.io' in str(remote_url)
            _test_url = str(remote_url) + '/foobar'
            assert urlopen(_test_url).read() == b'ok'
        pytest.raises(HTTPError, urlopen, _test_url)
    ```
    """
    managers = []

    def _wrap(port=None):
        manager = NgrokContextManager(_ngrok_bin, port, ngrok_authtoken)
        managers.append(manager)
        return manager()

    yield _wrap

    for m in managers:
        m.stop()
