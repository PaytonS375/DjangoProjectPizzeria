import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")

import django
django.setup()

from pizzas.models import *