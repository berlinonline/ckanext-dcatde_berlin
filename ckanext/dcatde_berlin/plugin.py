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
        config['ckanext.dcat.enable_content_negotiation'] = True
        config['ckanext.dcat.rdf.profiles'] = "euro_dcat_ap dcatap_de"
        config['ckanext.dcatde.contributorid'] = "berlinOpenData"
        config['ckanext.dcatde.version'] = "1.0.1"

    # -------------------------------------------------------------------
    # Implementation IBlueprint
    # -------------------------------------------------------------------

    def get_blueprint(self):
        return no_fisbroker_blueprint.no_fisbroker_api
    
