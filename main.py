# Django specific settings
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Using WSGI to be able to work with Django ORM
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#############

# Importing Django ORM
from data.models import *

# Add user
user = User(name="teste", email="vitor.fortunato@example.com")
user.save()

# Application logic
first_user = User.objects.all()[1]

print(first_user.name)
print(first_user.email)
