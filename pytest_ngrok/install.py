import io
import os
import re
import shutil
import subprocess
from urllib.request import urlopen
from zipfile import ZipFile


def fetch_url(url, stream_cls=io.BytesIO):
    stream = stream_cls()
    stream.write(urlopen(url).read())
    stream.seek(0)
    return stream


def get_bin_version(bin_path):
    process = subprocess.Popen(
        [
            bin_path,
            'version',
        ],
        stdout=subprocess.PIPE
    )
    process.wait()
    version_raw = process.stdout.readline().decode()

    return re.findall(r'(?:\d+\.)+\d+', version_raw)[0]


def install_bin(bin_path, remote_url):
    if os.path.exists(bin_path):
        raise ValueError("Path is exists!")
    dir_path = os.path.dirname(bin_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    zfile = ZipFile(fetch_url(remote_url))
    with open(bin_path, 'wb') as f:
        shutil.copyfileobj(zfile.open('ngrok'), f)
    os.chmod(bin_path, 0o755)
