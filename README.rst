.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/berlinonline/ckanext-dcatde_berlin.svg?branch=master
    :target: https://travis-ci.org/berlinonline/ckanext-dcatde_berlin

.. image:: https://coveralls.io/repos/berlinonline/ckanext-dcatde_berlin/badge.svg
  :target: https://coveralls.io/r/berlinonline/ckanext-dcatde_berlin

=============
ckanext-dcatde_berlin
=============

.. Put a description of your extension here:
This plugin implements dcat-ap.de_ for the Berlin open data portal
daten.berlin.de_.

It defines a profile ``dcatap_de`` that needs to be layered right on top of ``euro_dcat_ap``, as defined in ``ckanext-dcat`` (ckanextdcat_).

``ckanext-dcatde_berlin`` draws heavily on ``ckanext-dcatde`` (ckanext-dcatde_), but is separate, because the underlying CKAN schema isn't quite the same, and because ``ckanext-dcatde_berlin`` requires the CKAN DB to be converted before it can be used.

.. _ckanextdcat: https://github.com/ckan/ckanext-dcat
.. _dcat-ap.de: http://dcat-ap.de
.. _daten.berlin.de: https://daten.berlin.de
.. _ckanext-dcatde: https://github.com/GovDataOfficial/ckanext-dcatde

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

In the ``[app:main]`` section of your CKAN config file, add the following lines::

    ## DCAT
    ckanext.dcat.enable_content_negotiation = True
    ckanext.dcat.rdf.profiles = euro_dcat_ap dcatap_de
    ckanext.dcatde.contributorid = berlinOpenData
    ckanext.dcatde.version = 1.0.1


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
