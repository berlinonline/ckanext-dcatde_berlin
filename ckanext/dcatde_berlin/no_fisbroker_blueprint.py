from flask import Blueprint, make_response

from ckan.plugins import toolkit
from ckan.views.home import index

from ckanext.dcat.utils import check_access_header, CONTENT_TYPES

def read_catalog(format):

    if not format:
        format = check_access_header()

    if not format:
        return index()

    data_dict = {
        'page': toolkit.request.params.get('page'),
        'modified_since': toolkit.request.params.get('modified_since'),
        'format': format,
        'fq': '-berlin_source:harvest-fisbroker',
    }

    toolkit.response.headers.update(
        {'Content-type': CONTENT_TYPES[format]})
    try:
        return toolkit.get_action('dcat_catalog_show')({}, data_dict)
    except toolkit.ValidationError as ve:
        toolkit.abort(409, str(ve))


no_fisbroker_api = Blueprint('snippetapi', __name__)
no_fisbroker_api.add_url_rule(u'/catalog_no_fb.<format>',
                        methods=[u'GET'], view_func=read_catalog)

#     _map.connect('dcat_catalog_no_fb',
#                  '/catalog_no_fb.{_format}',
#                  controller=controller, action='read_catalog',
#                  requirements={'_format': 'xml|rdf|n3|ttl|jsonld'})
