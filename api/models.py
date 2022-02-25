from django.db import models
from tastypie.resources import ModelResource
from tools.models import Tool


# Create your models here.
class ToolResource(ModelResource):
    class Meta:
        queryset = Tool.objects.all()
        resource_name = 'tools'
