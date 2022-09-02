from import_export import resources
from .models import *

class PersonResource(resources.ModelResource):
    class meta:
        model = Person