from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(JobSeeker)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Profile)