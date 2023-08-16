from django.urls import path
from .views import CustomerServiceRequestView, RequestTrackingView 


urlpatterns = [
    path('create-service-request', CustomerServiceRequestView.as_view(), name="servicerequest"),
    path('request-tracking', RequestTrackingView.as_view(), name="requesttracking")
]

