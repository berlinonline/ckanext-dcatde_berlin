# Changelog

## Development

## 0.2.0

- Add changelog.
- Remove `dct:publisher` statements based on the CKAN organization, as that is only used internally to control access rights. There are organizations like "Simplesearch" or "FIS-Broker Harvester" that don't make sense as a publisher.
- Add information from `berlin_source` field as [dct:accrualMethod](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/2012-06-14/?v=terms#terms-accrualMethod).

## 0.1.0

- Initial version of the plugin