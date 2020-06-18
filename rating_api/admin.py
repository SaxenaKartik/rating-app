from django.contrib import admin
from rating_api import models
# Register your models here.

admin.site.register(models.MyUser)
admin.site.register(models.Product)
admin.site.register(models.Rate)
