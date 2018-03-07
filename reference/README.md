# Codelist Reference 

This folder contains RDF representations of codelists which are used by DCAT-AP and DCAT-AP.de.


## DCAT-AP.de Vokabulare

The original versions are published in RDF/XML. They are included here as Turtle, which is much more readable.

**Common prefix: `http://dcat-ap.de/def/`.**

| URI prefix | Filename | Web source |
| ---------- | -------- | ---------- |
| `licenses/`  | [`licenses-1_0.ttl`](dcat-ap.de/licenses-1_0.ttl) | [Lizenzen](http://www.dcat-ap.de/def/licenses/) |


## Metadata Registry - Named Authority Lists

[Named Authority Lists](http://publications.europa.eu/mdr/authority/index.html) from the EU's Metadata Registry.

They're included here because sadly, despite the fact that they're made available as RDF, the URIs used for the codes are not dereferenceable. This means you cannot "follow your nose" when you encounter them in our data. You have to manually look for them with a search engine to find the definitions, which defeats the purpose of using URIs as a tool for look-up.

The original versions are published in RDF/XML. They are included here as Turtle, which is much more readable.

**Common prefix: `http://publications.europa.eu/resource/authority/`**

| URI prefix | Filename | Web source |
| ---------- | -------- | ---------- |
| `language/`  | [`languages-skos-ap-act.ttl`](mdr-nal/languages-skos-ap-act.ttl) | [Language](http://publications.europa.eu/mdr/authority/language/) |
| `data-theme/` | [`data-theme-skos-ap-act.ttl`](mdr-nal/data-theme-skos-ap-act.ttl) | [Publication Theme](http://publications.europa.eu/mdr/authority/data-theme/) |
| `file-type/` | [`filetypes-skos-ap-act.ttl`](mdr-nal/filetypes-skos-ap-act.ttl) | [File Type](http://publications.europa.eu/mdr/authority/file-type/) |


## daten.berlin.de Vocab

Not everything we need is covered by the codelists referenced in DCAT-AP and DCAT-AP.de. Additional terminology is defined in our own vocabulary.

**Common prefix: `https://daten.berlin.de/schema/`**

| URI prefix | Filename |
| ---------- | -------- |
| `dist-format/`  | [`berlin-def.ttl`](berlin/berlin-def.ttl) |