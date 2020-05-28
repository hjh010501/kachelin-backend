models = ['restaurant']

for model in models:
    __import__('backend.models.{}'.format(model))

