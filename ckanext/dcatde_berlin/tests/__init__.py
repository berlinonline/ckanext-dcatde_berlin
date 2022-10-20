import pytest

import ckan.tests.factories as factories
import ckan.tests.helpers as helpers

@pytest.fixture
def datasets():
    org = factories.Organization()
    datasets = []
    for x in range(5):
        datasets.append(factories.Dataset(owner_org=org['id']))

    return datasets

@pytest.fixture
def berlin_dataset(app):
    '''Fixture for a dataset that conforms to the Berlin CKAN metadata schema.'''
    # {'author': ['Missing value'], 'berlin_source': ['Missing value'], 'berlin_type': ['Missing value'], 'date_released': ['Missing value'], 'license_id': ['Missing value'], 'maintainer_email': ['Missing value'], 'extras': [{'key': ['There is a schema field with the same name']}], 'groups': ["Required field 'groups' not set."]}
    org = factories.Organization(name='harvester-fis-broker')
    group = factories.Group(name='arbeit')
    dataset = factories.Dataset(
        owner_org=org['id'],
        groups=[{'id': group['id'], 'name': group['name']}],
        geographical_coverage='Mitte',
        license_id='cc-zero',
        berlin_source='webform',
        author='KB-ODMAN',
        berlin_type='datensatz',
        date_released='2022-10-19',
        maintainer_email='opendata@kbodman.berlin.de',
        attribution_text='Die königlich berlinische Open-Data-Manufaktur',
    )
    factories.Resource(package_id=dataset["id"], format="CSV")
    factories.Resource(package_id=dataset["id"], format="UNKNOWN_FORMAT")
    return dataset
