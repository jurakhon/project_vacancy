from django.contrib import admin

from vacancy.models import Category, Job, Applicant

# Register your models here.
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Applicant)
