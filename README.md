# ckanext-odata

This CKAN extension provides a basic [OData 3.0](https://www.odata.org/documentation/odata-version-3-0/) endpoint for CKAN.

The endpoint requires data to be held in the CKAN Datastore.
An _OData Endpoint_ link is added to resources on their main dataset page.

### Installation

To install ckanext-odata:

1. Activate your CKAN virtual environment, for example:

```
. /usr/lib/ckan/default/bin/activate
```

2. Install the ckanext-odata Python package into your virtual environment:

```
pip install ckanext-odata
```

3. Add ``odata`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

```
sudo service apache2 reload
```

### Config Settings
Currently there are no required configuration for this extension.

### Development Installation

To install ckanext-odata for development, activate your CKAN virtualenv
and do:

```
git clone https://github.com/keitaroinc/ckanext-odata
cd ckanext-odata
python setup.py develop
```
