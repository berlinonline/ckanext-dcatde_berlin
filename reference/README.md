# Cannot Follow your Nose

This folder contains RDF representations of codelists which are used by DCAT-AP and DCAT-AP.de.

They're included here because sadly, despite the fact that they're made available as RDF, the URIs used for the codes are not dereferenceable. This means you cannot "follow your nose" when you encounter them in our data. You have to manually look for them with a search engine to find the definitions. Also, the original versions are in RDF/XML, while they are included here as Turtle, which is much more readable.

## DCAT-AP.de Vokabulare

The common prefix is: `http://dcat-ap.de/def/`.

| URI prefix | Filename | Web source |
| ---------- | -------- | ---------- |
| `licenses/`  | [`licenses-1_0.ttl`](dcat-ap.de/licenses-1_0.ttl) | [Lizenzen](http://www.dcat-ap.de/def/licenses/) |


## Metadata Registry - Named Authority Lists

[Named Authority Lists](http://publications.europa.eu/mdr/authority/index.html) from the EU's Metadata Registry.

The common prefix is: `http://publications.europa.eu/resource/authority/`

| URI prefix | Filename | Web source |
| ---------- | -------- | ---------- |
| `language/`  | [`languages-skos-ap-act.ttl`](mdr-nal/languages-skos-ap-act.ttl) | [Language](http://publications.europa.eu/mdr/authority/language/) |
| `data-theme/` | [`data-theme-skos-ap-act.ttl`](mdr-nal/data-theme-skos-ap-act.ttl) | [Publication Theme](http://publications.europa.eu/mdr/authority/data-theme/) |
| `file-type/` | [`filetypes-skos-ap-act.ttl`](mdr-nal/filetypes-skos-ap-act.ttl) | [File Type](http://publications.europa.eu/mdr/authority/file-type/) |