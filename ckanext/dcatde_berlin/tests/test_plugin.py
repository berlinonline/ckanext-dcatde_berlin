"""Tests for plugin.py."""
import logging
import pytest

from ckanext.dcatde_berlin.tests import datasets

PLUGIN_NAME = 'dcatde_berlin'
LOG = logging.getLogger(__name__)

@pytest.mark.ckan_config('ckan.plugins', f'dcat {PLUGIN_NAME}')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestGeneralAvailability(object):

    def test_catalog_endpoint_available(self, app, datasets):
        '''Check that the catalog can be retrieved and do a few
           sanity checks.'''
        response = app.get(
            url="/catalog.ttl",
            follow_redirects=False,
            status=200,
        )

        assert f"hydra:totalItems {len(datasets)}" in response.body
        assert "a dcat:Catalog" in response.body
        assert "a dcat:Dataset" in response.body

    def test_dataset_endpoint_available(self, app, datasets):
        '''Check that the dataset endpoint is available and a dataset
           can be retrieved.'''
        dataset = datasets[0]
        response = app.get(
            url=f"/dataset/{dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert "a dcat:Dataset" in response.body
        assert f"dct:title \"{dataset['title']}\"" in response.body