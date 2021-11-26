import ckan.plugins as p

import ckanext.odata.actions as action
from ckan.lib.plugins import DefaultTranslation
import ckanext.odata.views as views


def link(resource_id):
    return '%s%s' % (action.base_url(), resource_id)


class ODataPlugin(p.SingletonPlugin, DefaultTranslation):

    p.implements(p.IConfigurer)
    p.implements(p.IActions)
    p.implements(p.ITemplateHelpers, inherit=True)
    p.implements(p.ITranslation)
    p.implements(p.IBlueprint)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('resources', 'odata')

    def get_actions(self):
        actions = {
            'ckanext-odata_odata': action.odata,
        }
        return actions

    def get_helpers(self):
        return {
            'ckanext_odata_link': link,
        }

    # IBlueprint

    def get_blueprint(self):
        return views.get_blueprints()
