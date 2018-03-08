# This Makefile automates some aspects of building ckanext-dcatde_berlin,
# such as generating mapping files from external sources

# requirements:
# - csvkit (http://csvkit.readthedocs.io/en/1.0.2/)
# - Jena command line tools: http://jena.apache.org

FILE-TYPE-NAL=reference/mdr-nal/filetypes-skos-ap-act.ttl
BERLIN-VOCAB=reference/berlin/berlin-def.ttl

QUERY-FORMAT-MAPPING-NAL=queries/file_format_mapping_nal.rq
QUERY-FORMAT-MAPPING-BERLIN=queries/file_format_mapping_berlin.rq

FORMAT-MAPPING-CSV=temp/filetypes.csv
FORMAT-MAPPING-CSV-NAL=temp/filetypes_nal.csv
FORMAT-MAPPING-CSV-BERLIN=temp/filetypes_berlin.csv

FORMAT-MAPPING-JSON=ckanext/dcatde_berlin/mappings/format_mapping.json

FORMAT-MAPPING-INDEX-COL=code

# we need Python 2
PYTHON=/usr/local/bin/python2

build-format-mappings: merge-format-mappings-csv
	$(PYTHON) bin/csv2json.py $(FORMAT-MAPPING-CSV) $(FORMAT-MAPPING-INDEX-COL) $(FORMAT-MAPPING-JSON)

merge-format-mappings-csv: query-format-mapping-nal query-format-mapping-berlin
	csvstack $(FORMAT-MAPPING-CSV-NAL) $(FORMAT-MAPPING-CSV-BERLIN) > $(FORMAT-MAPPING-CSV)

query-format-mapping-nal:
	@[ -d temp ] || mkdir temp
	sparql --query=$(QUERY-FORMAT-MAPPING-NAL) --data=$(FILE-TYPE-NAL) --results=CSV > $(FORMAT-MAPPING-CSV-NAL)

query-format-mapping-berlin:
	@[ -d temp ] || mkdir temp
	sparql --query=$(QUERY-FORMAT-MAPPING-BERLIN) --data=$(BERLIN-VOCAB) --results=CSV > $(FORMAT-MAPPING-CSV-BERLIN)

clean:
	@rm -rf temp

.PHONY: clean