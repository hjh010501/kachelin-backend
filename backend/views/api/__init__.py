apis = ['restaurant', 'review']

for api in apis:
    __import__('backend.views.api.{}'.format(api))