from django.contrib import admin
from .models import CustomerServiceRequest, RequestTracking
# Register your models here.
admin.site.register(CustomerServiceRequest)
admin.site.register(RequestTracking)