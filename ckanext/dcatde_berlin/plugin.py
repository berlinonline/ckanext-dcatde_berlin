# coding: utf-8

import os
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.dcatde_berlin import no_fisbroker_blueprint

class Dcatde_BerlinPlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IBlueprint, inherit=True)

    # -------------------------------------------------------------------
    # Implementation IConfigurer
    # -------------------------------------------------------------------

    def update_config(self, config):
        config['ckanext.dcat.enable_content_negotiation'] = config.get(
        'ckanext.dcat.enable_content_negotiation', True)
        config['ckanext.dcat.rdf.profiles'] = config.get(
        'ckanext.dcat.rdf.profiles', 'euro_dcat_ap_2 dcatap_de')
        config['ckanext.dcatde.contributorid'] = config.get(
        'ckanext.dcatde.contributorid','berlinOpenData')
        config['ckanext.dcatde.version'] = config.get(
        'ckanext.dcatde.version', '2.0')
        config['ckanext.dcatde_berlin.formats'] = config.get(
        'ckanext.dcatde_berlin.formats', 'ttl xml jsonld rdf')
        config['ckanext.dcatde_berlin.additional_endpoints'] = config.get(
        'ckanext.dcatde_berlin.additional_endpoints', f'/{no_fisbroker_blueprint.CATALOG_ENDPOINT_PATH}')

    # -------------------------------------------------------------------
    # Implementation IBlueprint
    # -------------------------------------------------------------------

    def get_blueprint(self):
        return no_fisbroker_blueprint.no_fisbroker_api
    
