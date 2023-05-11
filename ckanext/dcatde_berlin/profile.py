# -*- coding: utf-8 -*-

import os
import json
import logging

from rdflib import URIRef, BNode, Literal
from rdflib.namespace import Namespace
from rdflib.namespace import RDF, RDFS

from ckan.common import config

from ckanext.dcat.profiles import RDFProfile
from ckanext.dcat.utils import resource_uri

log = logging.getLogger(__name__)

# copied from ckanext.dcat.profiles
DCT = Namespace("http://purl.org/dc/terms/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
SCHEMA = Namespace('http://schema.org/')
TIME = Namespace('http://www.w3.org/2006/time')
LOCN = Namespace('http://www.w3.org/ns/locn#')
GSP = Namespace('http://www.opengis.net/ont/geosparql#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
SPDX = Namespace('http://spdx.org/rdf/terms#')
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
VOID = Namespace('http://rdfs.org/ns/void#')

# own namespaces
MDRLANG = Namespace('http://publications.europa.eu/resource/authority/language/')
MDRTHEME = Namespace('http://publications.europa.eu/resource/authority/data-theme/')
DCATDE = Namespace("http://dcat-ap.de/def/dcatde/")
DCATDE_LIC = Namespace("http://dcat-ap.de/def/licenses/")
DCATDE_CONTRIBUTORS = Namespace("http://dcat-ap.de/def/contributors/")

ACCRUAL_METHODS = Namespace("https://daten.berlin.de/ns/dcatext/accrual#")

namespaces = {
    # copied from ckanext.dcat.profiles
    'dct': DCT,
    'dcat': DCAT,
    'adms': ADMS,
    'vcard': VCARD,
    'foaf': FOAF,
    'schema': SCHEMA,
    'time': TIME,
    'skos': SKOS,
    'locn': LOCN,
    'gsp': GSP,
    'owl': OWL,
    'void': VOID,
    'mdrlang': MDRLANG ,
    'mdrtheme': MDRTHEME ,
    'dcatde': DCATDE ,
    'dcatde-lic': DCATDE_LIC ,
    'contributor': DCATDE_CONTRIBUTORS ,
    'accrual': ACCRUAL_METHODS ,
}

class DCATdeBerlinProfile(RDFProfile):
    '''
    An RDF profile for the that implements DCAT-AP.de, specifically
    for the Berlin data portal.

    It requires the European DCAT-AP profile (`euro_dcat_ap`)
    '''

    def __init__(self, graph, compatibility_mode=False):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)

        with open(os.path.join(dir_path, "mappings", "categories.json")) as json_data:
            self.category_mapping = json.load(json_data)

        with open(os.path.join(dir_path, "mappings", "licenses.json")) as json_data:
            self.license_mapping = json.load(json_data)

        with open(os.path.join(dir_path, "mappings", "geo_coverage.json")) as json_data:
            self.geo_coverage = json.load(json_data)

        with open(os.path.join(dir_path, "mappings", "org2legalBasis.json")) as json_data:
            self.legalBasis = json.load(json_data)

        with open(os.path.join(dir_path, "mappings", "format_mapping.json")) as json_data:
            self.format_mapping = json.load(json_data)

        super(DCATdeBerlinProfile, self).__init__(graph, compatibility_mode)

    def graph_from_dataset(self, dataset_dict, dataset_ref):

        log.debug("dataset: {}".format(dataset_dict['name']))
        g = self.g

        dist_additons = {}

        # bind namespaces to have readable names in RDF Document
        for prefix, namespace in namespaces.items():
            g.bind(prefix, namespace)

        # TEMPORARY: fix whitespace in 'url':
        url = dataset_dict['url']
        if url:
            g.remove( (dataset_ref, DCAT.landingPage, URIRef(url)) )
            url = url.replace(" ", "+")
            g.add( (dataset_ref, DCAT.landingPage, URIRef(url)) )

        # Nr. 40 - Contributor
        contributorId = config.get('ckanext.dcatde.contributorid')
        if contributorId:
            g.add((dataset_ref, DCATDE.contributorID, URIRef("{}{}".format(DCATDE_CONTRIBUTORS, contributorId))))

        # Nr. 44 - Publisher
        publisher_ref = BNode()
        publisher_name = self._get_dataset_value(dataset_dict, 'author')
        publisher_url = self._get_dataset_value(dataset_dict, 'url')
        # first, remove the publishers added by the generic RDF profile, as they
        # are based on the CKAN Organization
        for publisher in g.objects(dataset_ref, DCT.publisher):
            g.remove( (dataset_ref, DCT.publisher, publisher) )

        g.add( (publisher_ref, RDF.type, FOAF.Organization) )
        g.add( (publisher_ref, FOAF.name, Literal(publisher_name)) )
        # if publisher_url:
        #     g.add( (publisher_ref, FOAF.homepage, URIRef(publisher_url)) )
        g.add( (dataset_ref, DCT.publisher, publisher_ref) )

        # Nr. 45 - Kategorie
        groups = self._get_dataset_value(dataset_dict, 'groups')
        for group in groups:
            dcat_groups = self.category_mapping.get(group['name'], None)
            if dcat_groups is not None:
                for dcat_group in dcat_groups:
                    g.add( (dataset_ref, DCAT.theme, MDRTHEME[dcat_group]) )
                    # MDRTHEME.xyz is not dereferencable, so we add some additional
                    # triples that link to the downloadable source:
                    g.add( (MDRTHEME[dcat_group], RDFS.isDefinedBy, URIRef(MDRTHEME)) )
                    g.add( (URIRef(MDRTHEME), RDFS.seeAlso, URIRef("http://publications.europa.eu/mdr/resource/authority/data-theme/skos-ap-eu/data-theme-skos-ap-act.rdf")) )



        # Nr. 48 - conformsTo (Application Profile der Metadaten)
        dcatapde_version = config.get('ckanext.dcatde.version')
        if dcatapde_version:
            g.add((dataset_ref, DCT.conformsTo, URIRef("{}{}/".format(DCATDE, dcatapde_version))))

        # Nr. 49 - 52 (Urheber, Verwalter, Bearbeiter, Autor) - we don't know this

        # Nr. 59 - Sprache
        g.add( (dataset_ref, DCT.language, MDRLANG.DEU) )
        # MDRLANG.DEU is not dereferencable, so we add some additional
        # triples that link to the downloadable source:
        g.add( (MDRLANG.DEU, RDFS.isDefinedBy, URIRef(MDRLANG)) )
        g.add( (URIRef(MDRLANG), RDFS.seeAlso, URIRef("http://publications.europa.eu/mdr/resource/authority/language/skos-ap-eu/languages-skos-ap-act.rdf")) )

        # Nr. 61 - Provenienz

        # TODO: geharvestete Datensätze kennzeichnen?

        # Nr. 66 - dct:spatial via geonames reference
        # Nr. 72 - dcatde:politicalGeocodingLevelURI
        # Nr. 73 - dcatde:politicalGeocodingURI
        # passt leider nur bedingt auf Berlin (nur federal, state, administrativeDistrict)

        geographical_coverage = self._get_dataset_value(dataset_dict, 'geographical_coverage')
        if geographical_coverage in self.geo_coverage:
            coverage_object = self.geo_coverage[geographical_coverage]
            if 'geonames' in coverage_object:
                g.add( (dataset_ref, DCT.spatial, URIRef(coverage_object['geonames'])) )
            if 'politicalGeocodingURI' in coverage_object:
                g.add( (dataset_ref, DCATDE.politicalGeocodingURI, URIRef(coverage_object['politicalGeocodingURI'])) )
            if 'politicalGeocodingLevelURI' in coverage_object:
                g.add( (dataset_ref, DCATDE.politicalGeocodingLevelURI, URIRef(coverage_object['politicalGeocodingLevelURI'])) )



        # Nr. 75 - dcatde:legalbasisText

        legalbasisText = self.legalBasis['default']
        org = dataset_dict.get('organization', {})
        if org and org['name'] in self.legalBasis['mapping']:
            legalbasisText = self.legalBasis['mapping'][org['name']]
        g.add( (dataset_ref, DCATDE.legalbasisText, Literal(legalbasisText)) )

        # Enhance Distributions
        ## License
        ogd_license_code = dataset_dict.get('license_id')
        if ogd_license_code in self.license_mapping:
            dist_additons['license_id'] = self.license_mapping[ogd_license_code]['dcatde-id']

        ## Attribution Text
        if 'attribution_text' in dataset_dict:
            dist_additons['attribution_text'] = dataset_dict.get('attribution_text')

        for resource_dict in dataset_dict.get('resources', []):
            for distribution in g.objects(dataset_ref, DCAT.distribution):
                # Match distribution in graph and resource in ckan-dict
                if str(distribution) == resource_uri(resource_dict):
                    self.enhance_distribution_resource(g, distribution, resource_dict, dist_additons)

        # custom:

        # add information about the technical source of this dataset (webform, simplesearch, harvester, etc.)

        source = self._get_dataset_value(dataset_dict, 'berlin_source')
        if (source):
            g.add( (dataset_ref, DCT.accrualMethod, ACCRUAL_METHODS[source]) )

    def enhance_distribution_resource(self, g, distribution_ref, resource_dict, dist_additons):

        # TEMPORARY: fix whitespace in 'url':
        url = resource_dict['url']
        if url:
            g.remove( (distribution_ref, DCAT.accessURL, URIRef(url)) )
            url = url.replace(" ", "+")
            g.add( (distribution_ref, DCAT.accessURL, URIRef(url)) )

        # Nr. 77 - License (derived from dataset license)
        if 'license_id' in dist_additons:
            g.add( (distribution_ref, DCT.license, DCATDE_LIC[dist_additons['license_id']]) )

        # Nr. 78 - Format
        for format_string in g.objects(distribution_ref, DCT['format']):
            g.remove( (distribution_ref, DCT['format'], Literal(format_string)) )
            format_string = format_string.toPython()
            if format_string in self.format_mapping:
                format_uri = self.format_mapping[format_string]['uri']
                g.add( (distribution_ref, DCT['format'], URIRef(format_uri)) )
            else:
                log.warning("No mapping found for format string '{}'".format(format_string))

        # Nr. 93 - dcatde:licenseAttributionByText
        if 'attribution_text' in dist_additons:
            g.add( (distribution_ref, DCATDE.licenseAttributionByText, Literal(dist_additons['attribution_text'])) )       

