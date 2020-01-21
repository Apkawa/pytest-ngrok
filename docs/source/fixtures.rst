Fixtures
========

``ngrok``  
~~~~~~~~~

An wrapper for run ``ngrok`` to port

Example:
""""""""


Use as callable

.. code-block:: python
    
    import pytest

    from urllib.request import urlopen

    def test_ngrok(ngrok, httpserver):
        httpserver.expect_request("/foobar").respond_with_data("ok")
        remote_url = ngrok(httpserver.port)
        assert urlopen(remote_url + "/foobar").read() == b'ok'



Use as context manager

.. code-block:: python

    import pytest

    from urllib.error import HTTPError
    from urllib.request import urlopen

    def test_ngrok_context_manager(ngrok, httpserver):
        # example local server
        httpserver.expect_request("/foobar").respond_with_data("ok")
        with ngrok(httpserver.port) as remote_url:
            _test_url = str(remote_url) + '/foobar'
            assert urlopen(_test_url).read() == b'ok'

        # Connection closes
        pytest.raises(HTTPError, urlopen, _test_url)


``live_server_ngrok``
~~~~~~~~~~~~~~~~~~~~~

If installed ``pytest-django`` - you can use ``live_server_ngrok``

Example
"""""""

.. code-block::

    def test_server(live_server_ngrok):
        assert live_server_ngrok.url.endswith('ngrok.io')




``ngrok_bin``
~~~~~~~~~~~~~

Trying find ``ngrok`` binary in PATH or set default to ``$HOME/.local/bin/ngrok``
Also use ``--ngrok-bin=/path/to/ngrok`` 

Example
"""""""

.. code-block:: python

    from pytest import fixture
    
    @fixture(scope='session')
    def ngrok_bin(request):
        ngrok_path = request.config.getoption('--ngrok-bin')
        if not ngrok_path:
            ngrok_path = '/tmp/ngrok'
        return ngrok_path


``ngrok_install_url`` 
~~~~~~~~~~~~~~~~~~~~~

Url for fetch binary if ``ngrok_bin`` not exists.
Default is ``https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip``

Example: 
""""""""

.. code-block:: python

    from pytest import fixture
    
    @fixture(scope='session')
    def ngrok_install_url():
        return 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'

``ngrok_allow_install``
~~~~~~~~~~~~~~~~~~~~~~~

Allow to fetch and install before test. Default is ``true``. You can set to ``false`` for forbid download binaries but m
Also use ``--ngrok-no-install``


Example
"""""""

.. code-block:: python

    from pytest import fixture

    @fixture(scope='session')
    def ngrok_allow_install(request):
        return true
