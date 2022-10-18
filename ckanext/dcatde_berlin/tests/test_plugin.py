"""Tests for plugin.py."""
import ckanext.dcatde_berlin.plugin as plugin

import logging
import pytest

PLUGIN_NAME = 'berlinauth'
LOG = logging.getLogger(__name__)

@pytest.mark.ckan_config('ckan.plugins', f'dcat {PLUGIN_NAME}')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestStuff(object):

    def test_catalog_available(self):
        pass