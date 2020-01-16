import os
import subprocess
import tempfile

from pytest_ngrok.install import install_bin


def test_install():
    bin_path = tempfile.mktemp()
    install_bin(bin_path)
    assert os.path.exists(bin_path)
    ver = subprocess.check_output([bin_path, 'version']).decode('utf-8')
    assert ver.startswith('ngrok version')
    os.unlink(bin_path)
