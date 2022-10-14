# ckanext-berlindcatde_berlinath

[![Tests](https://github.com/berlinonline/ckanext-dcatde_berlin/workflows/Tests/badge.svg?branch=master)](https://github.com/berlinonline/ckanext-dcatde_berlin/actions)
[![Code Coverage](http://codecov.io/github/berlinonline/ckanext-dcatde_berlin/coverage.svg?branch=master)](http://codecov.io/github/berlinonline/ckanext-dcatde_berlin?branch=master)

This plugin belongs to a set of plugins for the _Datenregister_ – the non-public [CKAN](https://ckan.org) instance that is part of Berlin's open data portal [daten.berlin.de](https://daten.berlin.de).

`ckanext-dcatde_berlin` pefines a profile ``dcatap_de`` that needs to be layered right on top of ``euro_dcat_ap``, as defined in [ckanext-dcat](https://github.com/ckan/ckanext-dcat).

`ckanext-dcatde_berlin` draws heavily on [ckanext-dcatde](https://github.com/GovDataOfficial/ckanext-dcatde), but is separate, because the underlying CKAN schema isn't quite the same, and because `ckanext-dcatde_berlin` requires the CKAN DB to be converted before it can be used.


The plugin implements the following CKAN interfaces:

- [IBlueprint](http://docs.ckan.org/en/latest/extensions/plugin-interfaces.html#ckan.plugins.interfaces.IBlueprint)

## Requirements

This plugin has been tested with CKAN 2.9.5 (which requires Python 3).
