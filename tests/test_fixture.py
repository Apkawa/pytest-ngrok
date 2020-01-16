# -*- coding: utf-8 -*-
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

from pytest_ngrok.manager import NgrokContextManager


def test_ngrok_plugin(ngrok, httpserver):
    httpserver.expect_request("/foobar").respond_with_data("ok")

    remote_url = ngrok(httpserver.port)
    assert isinstance(remote_url, NgrokContextManager)
    assert (remote_url + '/123').endswith('/123')
    assert 'ngrok.io' in str(remote_url)
    _test_url = str(remote_url) + '/foobar'

    assert urlopen(_test_url).read() == b'ok'
    remote_url.stop()

    pytest.raises(HTTPError, urlopen, _test_url)


def test_ngrok_multiple_instances(ngrok, httpserver):
    httpserver.expect_request("/1").respond_with_data("1")
    httpserver.expect_request("/2").respond_with_data("2")

    remote_url_1 = ngrok(httpserver.port)
    remote_url_2 = ngrok(httpserver.port)

    assert remote_url_1 != remote_url_2

    assert urlopen(remote_url_1 + '/1').read() == b'1'
    assert urlopen(remote_url_2 + '/2').read() == b'2'
