from django.db import models

class ServiceTypes(models.TextChoices):
    GAS_LEAK_ISSUE = "Gas Leak Issue"
    METER_INSTALLATION = "Meter Installation"
    GAS_PRESSURE = "Gas Pressure Adjustment"
    GAS_VENTILATION_ISSUES = "Gas Ventilation Issues"

class RequestStatus(models.TextChoices):
    SUBMITTED = "Submitted"
    IN_PROGRESS_AND_REVIEW = "In Progress Review"
    ASSIGNED_PARTNER = "Assigned Partner" #it might be home/office check-up person
    ISSUE_RESOLVED = "Issue Resolved"
    REQUEST_TESTING = "Request Testing"
    RECHECK_ISSUE = "Recheck Issue"
    REQUEST_CLOSED = "Request Closed"