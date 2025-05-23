'''Tests to determine if the profile's conversion code works correctly.'''

import logging
import urllib.parse
from email.mime import base
from os import path

import ckan.tests.factories as factories
import pytest
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCAT, DCTERMS, RDF

from ckanext.dcatde_berlin.tests import (
    HVD_CODE,
    berlin_dataset,
    datasets,
    fisbroker_datasets,
    hvd_dataset_tag,
)
from ckanext.dcatde_berlin.profile import DCATdeBerlinProfile


PLUGIN_NAME = 'dcatde_berlin'
LOG = logging.getLogger(__name__)

DCATDE = Namespace('http://dcat-ap.de/def/dcatde/')
DCATDE_LIC = Namespace('http://dcat-ap.de/def/licenses/')
FILE_TYPES = Namespace('http://publications.europa.eu/resource/authority/file-type/')
HVD = Namespace('http://data.europa.eu/bna/')
MDRTHEME = Namespace('http://publications.europa.eu/resource/authority/data-theme/')
MUSTERD = Namespace('https://musterdatenkatalog.de/def/musterdatensatz/')

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

    @pytest.mark.parametrize("data", [
        {
            'ckan_license_id': 'dl-zero-de/2.0',
            'expected': 'dl-zero-de/2.0'
        },
        {
            'ckan_license_id': 'dl-de-zero-2.0',
            'expected': 'dl-zero-de/2.0'
        },
        {
            'ckan_license_id': 'CC BY 3.0 DE',
            'expected': 'cc-by-de/3.0'
        },
        {
            'ckan_license_id': 'cc-by/4.0',
            'expected': 'cc-by/4.0'
        }
    ])
    def test_license_id_mapping(self, data):
        profile = DCATdeBerlinProfile(graph=Graph())
        assert profile.map_license_code(data['ckan_license_id']) == data['expected']

@pytest.mark.ckan_config('ckan.plugins', f'dcat {PLUGIN_NAME} berlin_dataset_schema')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestProfileWithSchema(object):

    def test_group_was_mapped(self, app, berlin_dataset):
        '''Check that the dataset's group/category has been mapped to an MDR theme.'''
        dataset = berlin_dataset['dataset']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        dataset_res = URIRef(path.join(base_url, 'dataset', dataset['id']))
        mdr_theme_code = "ECON"
        assert (dataset_res, DCAT.theme, MDRTHEME[mdr_theme_code]) in g

    def test_geo_coverage_was_mapped(self, app, berlin_dataset):
        '''Check that the geographical coverage was mapped to various LOD URIs.'''
        dataset = berlin_dataset['dataset']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        dataset_res = URIRef(path.join(base_url, 'dataset', dataset['id']))
        assert (dataset_res, DCTERMS.spatial, URIRef('http://dcat-ap.de/def/politicalGeocoding/regionalKey/110010001001')) in g
        assert (dataset_res, DCATDE.politicalGeocodingLevelURI, URIRef('http://dcat-ap.de/def/politicalGeocoding/Level/administrativeDistrict')) in g
        assert (dataset_res, DCTERMS.spatial, URIRef('http://www.geonames.org/2870912')) in g
        assert (dataset_res, DCTERMS.spatial, URIRef('https://berlinonline.github.io/lod-berlin-lor/bez_01')) in g

    def test_legal_basis_was_mapped(self, app, fisbroker_datasets):
        '''Check that, in certain cases, the legal basis for publishing Open Data has been derived from the organization.'''
        dataset = fisbroker_datasets['fb'][0]
        response = app.get(
            url=f"/dataset/{dataset['name']}.ttl",
            follow_redirects=False,
            status=200,
        )
        assert "Nutzungsbestimmungen für die Bereitstellung von Geodaten des Landes Berlin (GeoNutzV-Berlin)" in response.body

    def test_license_id_was_mapped(self, app, berlin_dataset):
        '''Check that the license_id was mapped to a dcat-ap.de license URI.'''
        dataset = berlin_dataset['dataset']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        csv_resource = get_resource(base_url, dataset, berlin_dataset['csv_resource'])
        assert (csv_resource, DCTERMS.license, DCATDE_LIC['cc-zero']) in g

    def test_attribution_text_was_mapped(self, app, berlin_dataset):
        '''Check that the dataset's attribution text was mapped.'''
        dataset = berlin_dataset['dataset']
        attribution_text = dataset['attribution_text']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        csv_resource = get_resource(base_url, dataset, berlin_dataset['csv_resource'])
        assert (csv_resource, DCATDE.licenseAttributionByText, Literal(attribution_text)) in g

    def test_format_was_mapped(self, app, berlin_dataset):
        '''Check that the dataset's resource format string was mapped to a URI.'''
        dataset = berlin_dataset['dataset']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        csv_resource = get_resource(base_url, dataset, berlin_dataset['csv_resource'])
        assert (csv_resource, DCTERMS.format, FILE_TYPES.CSV) in g

    def test_references(self, app, berlin_dataset):
        '''Check that the dataset's references (HVD and Musterdatensatz) are included.'''
        dataset = berlin_dataset['dataset']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        dataset_res = URIRef(path.join(base_url, 'dataset', dataset['id']))
        hvd_res = HVD[dataset['hvd_category']]
        assert (dataset_res, DCTERMS.references, hvd_res) in g
        sample_record_res = MUSTERD[dataset['sample_record']]
        assert (dataset_res, DCTERMS.references, sample_record_res) in g

    def test_references_from_tag(self, app, hvd_dataset_tag):
        '''Check that specific HVD tags have been included as `dct:references` statements.'''
        dataset = hvd_dataset_tag['dataset']
        g, base_url = get_graph_and_base_url(app, dataset['name'])
        dataset_res = URIRef(path.join(base_url, 'dataset', dataset['id']))
        hvd_res = HVD[f'c_{HVD_CODE}']
        assert (dataset_res, DCTERMS.references, hvd_res) in g

def get_graph_and_base_url(app, package_name: str) -> tuple[Graph, str]:
    response = app.get(
        url=f"/dataset/{package_name}.ttl",
        follow_redirects=False,
        status=200,
    )
    g = Graph()
    g.parse(data=response.body)
    base_url = get_base_url(g)
    return (g, base_url)

def get_resource(base_url, package_dict, resource_dict) -> URIRef:
    csv_resource_uri = path.join(base_url, 'dataset', package_dict['id'], 'resource', resource_dict['id'])
    return URIRef(csv_resource_uri)



def get_base_url(g: Graph)->str:
    dataset_res = next(g.subjects(RDF.type, DCAT.Dataset)).toPython()
    path = urllib.parse.urlparse(dataset_res).path
    return dataset_res.split(path)[0]