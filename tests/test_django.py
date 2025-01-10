from urllib.request import urlopen

import pytest

try:
    import pytest_django
except ImportError:
    pytest_django = None


@pytest.mark.skipif(not pytest_django, reason="django and pytest-django not installed")
def test_server(live_server_ngrok):
    assert live_server_ngrok.url.endswith("ngrok.io")
    assert live_server_ngrok.remote_url.endswith("ngrok.io")
    assert live_server_ngrok.local_url.startswith("http://localhost:")
    assert urlopen(live_server_ngrok.local_url).read() == b"OK"
    assert urlopen(live_server_ngrok.remote_url).read() == b"OK"
