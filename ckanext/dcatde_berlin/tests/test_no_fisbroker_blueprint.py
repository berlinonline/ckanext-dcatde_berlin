"""Tests for no_fisbroker_plugin.py."""
import logging
import pytest

from ckanext.dcatde_berlin.tests import fisbroker_datasets

PLUGIN_NAME = 'dcatde_berlin'
LOG = logging.getLogger(__name__)

@pytest.mark.ckan_config('ckan.plugins', f'dcat {PLUGIN_NAME}')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestGeneralAvailability(object):

    def test_only_non_fisbroker_datasets_returned(self, app, fisbroker_datasets):
        '''Check that the special no-fisbroker-endpoint returns only
           non-fisbroker datasets.'''
        response = app.get(
            url="/catalog_no_fb.ttl",
            follow_redirects=False,
            status=200,
        )
        # TODO: check only non-fb datasets are returned

    def test_invalid_format(self, app):
        '''Check that calling the no-fisbroker-endpoint leads to a 409 error.'''
        response = app.get(
            url="/catalog_no_fb.foo",
            follow_redirects=False,
            status=409,
        )

    def test_empty_format(self, app):
        '''Check that calling the no-fisbroker-endpoint with no format parameter to a 409 error.'''
        response = app.get(
            url="/catalog_no_fb",
            status=409,
        )

