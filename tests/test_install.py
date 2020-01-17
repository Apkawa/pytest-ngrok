import os
import subprocess
import tempfile

from pytest_ngrok.install import install_bin
from pytest_ngrok.plugin import REMOTE_URL


def test_install():
    bin_path = tempfile.mktemp()
    install_bin(bin_path, remote_url=REMOTE_URL)
    assert os.path.exists(bin_path)
    ver = subprocess.check_output([bin_path, 'version']).decode('utf-8')
    assert ver.startswith('ngrok version')
    os.unlink(bin_path)
