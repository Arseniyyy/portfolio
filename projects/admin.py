from django.contrib import admin
from .models import project_models


for model in project_models:
    admin.site.register(model)
