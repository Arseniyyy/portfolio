import os
from django.conf import settings

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=20, default='Test')
    description = models.TextField(blank=True, default='Test')
    technology = models.CharField(max_length=20, blank=True, default='Django')
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True)
    url = models.URLField(unique=True, blank=True)

    def __str__(self) -> str:
        return self.title


project_models = [
    Project
]
