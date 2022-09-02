from django.test import TestCase

from core.users.models import *


# user
u = User()
u.first_name = 'Muisne'
u.last_name = 'Muisne'
u.username = 'admin'
u.dni = '1723598502'
u.email = 'muisne@muisne.com'
u.is_active = True
u.is_superuser = True
u.is_staff = True
u.set_password('admin')
u.save()