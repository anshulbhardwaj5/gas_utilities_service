from django.db import models
from django.contrib.auth.models import AbstractUser
from .enum import ServiceTypes, RequestStatus
from model_utils.models import TimeStampedModel
# Create your models here.

class User(AbstractUser):
    ...

class CustomerServiceRequest(TimeStampedModel): 
    service_title = models.CharField(max_length=100, blank=True, null=True)
    CUSTOMER_REQUEST_TYPE = [
        ("Gas Leak Issue", "Gas Leak Issue"),
        ("Meter Installation", "Meter Installation"),
        ("Gas Pressure Adjustment", "Gas Pressure Adjustment"),
        ("Gas Ventilation Issues", "Gas Ventilation Issues"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_service = models.CharField(choices=CUSTOMER_REQUEST_TYPE, default="Gas Leak Issue", max_length=100)

    REQUEST_STATUSES = [
        ("Completed", "Completed"),
        ("Submitted","Submitted"),
        ("In Progress Review", "In Progress Review"),
        ("Assigned Partner", "Assigned Partner"),
        ("Issue Resolved", "Issue Resolved"),
        ("Request Testing", "Request Testing"),
        ("Recheck Issue", "Recheck Issue"),
        ("Request Closed", "Request Closed"),
        ]   

    service_details = models.TextField(default="No details provided", blank=True, max_length=1000, null=True)
    request_status = models.CharField(choices=REQUEST_STATUSES, blank=True, null=True, max_length=100)
    attach_files = models.CharField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.service_title

class RequestTracking(TimeStampedModel): 
    REQUEST_STATUSES = [
    ("Completed", "Completed"),
    ("Submitted","Submitted"),
    ("In Progress Review", "In Progress Review"),
    ("Assigned Partner", "Assigned Partner"),
    ("Issue Resolved", "Issue Resolved"),
    ("Request Testing", "Request Testing"),
    ("Recheck Issue", "Recheck Issue"),
    ("Request Closed", "Request Closed"),
    ]   

    partner_assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partner')
    customer_request = models.ForeignKey(CustomerServiceRequest, on_delete=models.CASCADE, related_name='request')
    request_status = models.CharField(choices=REQUEST_STATUSES, default="In Progress Review", blank=True, null=True, max_length=100)
    request_resolved_time = models.DateTimeField(auto_now_add= False)

    def __str__(self) -> str:
        return self.customer_request.service_title
