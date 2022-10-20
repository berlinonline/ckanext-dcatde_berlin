'''Tests to determine if the profile's conversion code works correctly.'''

import logging
import pytest

import ckan.tests.factories as factories

from ckanext.dcatde_berlin.tests import datasets, berlin_dataset

PLUGIN_NAME = 'dcatde_berlin'
LOG = logging.getLogger(__name__)

@pytest.mark.ckan_config('ckan.plugins', f'dcat {PLUGIN_NAME}')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestProfileWithoutSchema(object):

    def test_no_spaces_in_url(self, app, berlin_dataset):
        '''Check that spaces in the `url` have been replaced with plus signs.'''
        org = factories.Organization()
        dataset = factories.Dataset(
            owner_org=org['id'],
            url="http://example.com/data/this has spaces"
        )
        response = app.get(
            url=f"/dataset/{dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert dataset['url'].replace(" ", "+") in response.body


@pytest.mark.ckan_config('ckan.plugins', f'dcat {PLUGIN_NAME} berlin_dataset_schema')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestProfileWithSchema(object):

    def test_group_was_mapped(self, app, berlin_dataset):
        '''Check that the dataset's group/category has been mapped to an MDR theme.'''
        response = app.get(
            url=f"/dataset/{berlin_dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        mdr_theme_code = "ECON"
        assert f"dcat:theme mdrtheme:{mdr_theme_code}" in response.body

    def test_geo_coverage_was_mapped(self, app, berlin_dataset):
        '''Check that the geographical coverage was mapped to various LOD URIs.'''
        response = app.get(
            url=f"/dataset/{berlin_dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert 'dcatde:politicalGeocodingURI <http://dcat-ap.de/def/politicalGeocoding/regionalKey/110010001001>' in response.body
        assert 'dcatde:politicalGeocodingLevelURI <http://dcat-ap.de/def/politicalGeocoding/Level/administrativeDistrict>' in response.body
        assert 'dct:spatial <http://www.geonames.org/2870912>' in response.body

    def test_legal_basis_was_mapped(self, app, berlin_dataset):
        '''Check that, in certain cases, the legal basis for publishing Open Data has been derived from the organization.'''
        response = app.get(
            url=f"/dataset/{berlin_dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert "Nutzungsbestimmungen für die Bereitstellung von Geodaten des Landes Berlin (GeoNutzV-Berlin)" in response.body

    def test_license_id_was_mapped(self, app, berlin_dataset):
        '''Check that the license_id was mapped to a dcat-ap.de license URI.'''
        response = app.get(
            url=f"/dataset/{berlin_dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert "dct:license dcatde-lic:cc-zero" in response.body

    def test_attribution_text_was_mapped(self, app, berlin_dataset):
        '''Check that the dataset's attribution text was mapped.'''
        attribution_text = berlin_dataset['attribution_text']
        response = app.get(
            url=f"/dataset/{berlin_dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert f"dcatde:licenseAttributionByText \"{attribution_text}\"" in response.body

    def test_format_was_mapped(self, app, berlin_dataset):
        '''Check that the dataset's resource format string was mapped to a URI.'''
        response = app.get(
            url=f"/dataset/{berlin_dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert f"dct:format <http://publications.europa.eu/resource/authority/file-type/CSV>" in response.body

