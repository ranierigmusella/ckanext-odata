from flask import Blueprint

import ckan.plugins as p

odata_blueprint = Blueprint(u'odata_blueprint', __name__)


def odata(uri):
    data_dict = {'uri': uri}
    action = p.toolkit.get_action('ckanext-odata_odata')
    result = action({}, data_dict)
    return result


odata_blueprint.add_url_rule(u'/datastore/odata3.0/<path:uri>', view_func=odata)


def get_blueprints():
    return [odata_blueprint]
