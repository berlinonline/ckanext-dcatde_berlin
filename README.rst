.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/knudmoeller/ckanext-dcatde_berlin.svg?branch=master
    :target: https://travis-ci.org/knudmoeller/ckanext-dcatde_berlin

.. image:: https://coveralls.io/repos/knudmoeller/ckanext-dcatde_berlin/badge.svg
  :target: https://coveralls.io/r/knudmoeller/ckanext-dcatde_berlin

.. image:: https://pypip.in/download/ckanext-dcatde_berlin/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-dcatde_berlin/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-dcatde_berlin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-dcatde_berlin/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-dcatde_berlin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-dcatde_berlin/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-dcatde_berlin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-dcatde_berlin/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-dcatde_berlin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-dcatde_berlin/
    :alt: License

=============
ckanext-dcatde_berlin
=============

.. Put a description of your extension here:
   This plugin implements dcat-ap.de for the Berlin open data portal
   daten.berlin.de.


------------
Requirements
------------

``ckanext-dcatde_berlin`` has been tested with:

- CKAN v2.6.2
- ``ckanext-dcat``: v0.6.0


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-dcatde_berlin:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Clone ``ckanext-dcatde_berlin`` into your CKAN ``src`` folder from the git 
   repository.

3. Add ``dcatde_berlin`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.dcatde_berlin.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-dcatde_berlin for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/knudmoeller/ckanext-dcatde_berlin.git
    cd ckanext-dcatde_berlin
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.dcatde_berlin --cover-inclusive --cover-erase --cover-tests
