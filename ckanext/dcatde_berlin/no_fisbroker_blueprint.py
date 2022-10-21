from flask import Blueprint, make_response

from ckan.common import config
from ckan.plugins import toolkit
from ckan.views.home import index

from ckanext.dcat.utils import check_access_header, CONTENT_TYPES

def read_catalog(format=None):

    def validate_format(format):
        if format not in valid_formats:
            raise toolkit.ValidationError(f"{format} is not a valid format. Only {', '.join(valid_formats)} are supported.")

    valid_formats = config.get('ckanext.dcatde_berlin.formats').split()

    try:
        if not format:
            format = check_access_header()

        if not format:
            raise toolkit.ValidationError(f"Please specify a format: {', '.join(valid_formats)} are supported.")

        data_dict = {
            'page': toolkit.request.params.get('page'),
            'modified_since': toolkit.request.params.get('modified_since'),
            'format': format,
            'fq': '-berlin_source:harvest-fisbroker',
        }

        validate_format(format)
        response = toolkit.get_action('dcat_catalog_show')({}, data_dict)
    except toolkit.ValidationError as ve:
        toolkit.abort(409, str(ve))

    response = make_response(response)
    response.headers['Content-type'] = CONTENT_TYPES[format]

    return response


no_fisbroker_api = Blueprint('no_fisbroker_api', __name__)
no_fisbroker_api.add_url_rule(u'/catalog_no_fb.<format>',
                        methods=[u'GET'], view_func=read_catalog)
no_fisbroker_api.add_url_rule(u'/catalog_no_fb',
                        methods=[u'GET'], view_func=read_catalog)


