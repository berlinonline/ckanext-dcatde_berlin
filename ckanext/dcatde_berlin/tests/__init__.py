import pytest

import ckan.tests.factories as factories
import ckan.tests.helpers as helpers

HVD_CODE = 'e1da4e07'

@pytest.fixture
def datasets():
    org = factories.Organization()
    datasets = []
    for x in range(5):
        datasets.append(factories.Dataset(owner_org=org['id']))

    return datasets

@pytest.fixture
def fisbroker_datasets():
    org = factories.Organization()
    fb_org = factories.Organization(name='harvester-fis-broker')
    group = factories.Group(name='umwelt')
    datasets = {
        'non_fb': [],
        'fb': []
    }
    for x in range(5):
        datasets['non_fb'].append(factories.Dataset(
            owner_org=org['id'],
            groups=[{'id': group['id'], 'name': group['name']}],
            geographical_coverage='Mitte',
            license_id='cc-zero',
            berlin_source='webform',
            author='KB-ODMAN',
            berlin_type='datensatz',
            date_released=f'2022-10-{x+1:02}',
            maintainer_email='opendata@kbodman.berlin.de',
            attribution_text='Die königlich berlinische Open-Data-Manufaktur',
        ))
    for x in range(5):
        datasets['fb'].append(factories.Dataset(
            owner_org=fb_org['id'],
            groups=[{'id': group['id'], 'name': group['name']}],
            geographical_coverage='Mitte',
            license_id='cc-zero',
            berlin_source='harvester-fis-broker',
            author='KB-ODMAN',
            berlin_type='datensatz',
            date_released=f'2022-10-{x+1:02}',
            maintainer_email='opendata@kbodman.berlin.de',
            attribution_text='Die königlich berlinische Open-Data-Manufaktur',
        ))

    return datasets

@pytest.fixture
def berlin_dataset():
    '''Fixture for a dataset that conforms to the Berlin CKAN metadata schema.'''
    org = factories.Organization(name='koenigliche-open-data-manufaktur')
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
        hvd_category=f'c_{HVD_CODE}',
        sample_record='bildung/hochschule/studentenwohnheim',
    )
    csv_res = factories.Resource(package_id=dataset["id"], format="CSV")
    unknown_res = factories.Resource(package_id=dataset["id"], format="UNKNOWN_FORMAT")
    return {
        'dataset': dataset,
        'csv_resource': csv_res,
        'unknown_resource': unknown_res,
    }

@pytest.fixture
def hvd_dataset_tag():
    '''Fixture for a dataset that conforms to the Berlin CKAN metadata schema.'''
    org = factories.Organization(name='koenigliche-open-data-manufaktur')
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
        tags=[{'name': f'HVD_{HVD_CODE}'}],
    )
    csv_res = factories.Resource(package_id=dataset["id"], format="CSV")
    return {
        'dataset': dataset,
        'csv_resource': csv_res,
    }

