# Changelog

## Development

- Change modelling of HVD-categorisation to DCAT-AP.de 3.0:
  - Instead of using `dct:references`, use `dcatap:hvdCategory`.
  - Use `dcatap:applicableLegislation <http://data.europa.eu/eli/reg_impl/2023/138/oj>`.

## [0.3.9](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.9)

_(2025-05-07)_

- While at this stage we should expect good license codes, be more lenient in what we accept and handöe. In case we get one which is not in our standard list of codes, we should still give useful output in the DCAT-output.

## [0.3.8](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.8)

_(2025-03-28)_

- WFS and WMS resources are now output as a `dcat:DataService` and matching service distribution. See https://www.dcat-ap.de/def/dcatde/2.0/implRules/#modellierung-eines-datenservices.
- Ensure that there is always a maximum of one `locn:geometry` per `dct:Location`. It should be the one with datatype `gsp:wktLiteral`.
- Unit tests that check RDF output are now based on parsing with rdflib, rather than just looking for strings (which is brittle, because representations can differ).
- Use `euro_dcat_ap_2` as the base profile.
- Announce that we're outputting DCAT-AP.de 2.0.
- Check for presence of special tags/keywords with the pattern `HVD_{ID}` and add corresponding `dct:references` statements to output. This is to support the setting of high-value dataset categories for external data sources systems (e.g. harvested portals and Imperia) that do not (yet) have a mechanism for setting HVD catgories.

## [0.3.7](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.7)

_(2025-03-28)_

- Expose Musterdatensatz (sample record) with `dct:references` (see https://www.dcat-ap.de/def/dcatde/2.0/implRules/#verweis-auf-referenzobjekte).

## [0.3.6](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.6)

_(2025-03-27)_

- Expose HVD (high-value dataset) category with `dct:references` (see https://www.dcat-ap.de/def/dcatde/2.0/implRules/#verweis-auf-referenzobjekte).
- Fix license key for CC BY 4.0 in [licenses.json](ckanext/dcatde_berlin/mappings/licenses.json).

## [0.3.5](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.5)

_(2024-12-20)_

- Update config settings (read from .ini file or use default value if the variable is not set).
- Add OpenCode [publiccode.yml](publiccode.yml) file.
- Update README.

## [0.3.4](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.4)

_(2023-05-19)_

- Fix packaging to ensure VERSION file and mapping JSON files are included in built distributions.

## [0.3.3](https://github.com/berlinonline/ckanext-dcatde_berlin/releases/tag/0.3.3)

_(2023-05-11)_

- Set `ckanext.dcatde_berlin.additional_endpoints` in code, derived from the `catalog_no_fb` endpoint's blueprint.
- Fix bug where unknown groups/categories would lead to a key error.
- Define extension's version string in [VERSION](VERSION), make available as `ckanext.dcatde_berlin.__version__` and in [setup.py](setup.py).

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