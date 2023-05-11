# Changelog

## Development

- Set `ckanext.dcatde_berlin.additional_endpoints` in code, derived from the `catalog_no_fb` endpoint's blueprint.

## [0.3.2](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.2)

_(2023-01-25)_

- Fix changelog.
- Fix manifest.

## [0.3.1](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.1)

_(2022-10-25)_

- Change codecov upload in github CI, now using the recommended approach as defined in https://docs.codecov.com/docs#step-4-upload-coverage-reports-to-codecov

## [0.3.0](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.0)

_(2022-10-21)_

- Convert to Python 3.
- Replace IRoutes interface with IBlueprint.
- Add tests.
- Switch from RST to Markdown for Readme.
- Reformat changelog, add dates and version links.

## [0.2.1](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/v0.2.1)

_(2020-07-29)_

- Add a second DCAT `catalog` endpoint which returns only those datasets that were _not_ harveseted from FIS-Broker. URL is `/catalog_no_fb.{FORMAT}` (the regular endpoint is `/catalog.{FORMAT}`).
- Remove `ckanext-dcat` from `requirements.txt`, as this can cause conflicts with a manually installed version of the same library.

## [0.2.0](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/v0.2.0)

_(2019-12-13)_

- Add changelog.
- Remove `dct:publisher` statements based on the CKAN organization, as that is only used internally to control access rights. There are organizations like "Simplesearch" or "FIS-Broker Harvester" that don't make sense as a publisher.
- Add information from `berlin_source` field as [dct:accrualMethod](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/2012-06-14/?v=terms#terms-accrualMethod).

## [0.1.0](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/v0.1.0)

_(2018-07-12)_

- Initial version of the plugin