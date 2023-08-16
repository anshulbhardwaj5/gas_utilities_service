from .models import CustomerServiceRequest, RequestTracking
from rest_framework import serializers
from utils.aws_helper import Aws_helper

class CustomerServiceRequestSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        aws = Aws_helper()
        data = super().to_representation(instance)
        if instance.attach_files is not None:    
            aws_res_attach_files = aws.get_public_url(instance.attach_files)
            data['attach_files'] = aws_res_attach_files['link'] if aws_res_attach_files['link'] is not None else None
       
        return data    
    class Meta:
        model = CustomerServiceRequest
        fields = "__all__"

class RequestTrackingSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        aws = Aws_helper()
        data = super().to_representation(instance)
        if instance.attach_files is not None:    
            aws_res_attach_files = aws.get_public_url(instance.attach_files)
            data['attach_files'] = aws_res_attach_files['link'] if aws_res_attach_files['link'] is not None else None
       
        return data    
    class Meta:
        model = RequestTracking
        fields = "__all__"
