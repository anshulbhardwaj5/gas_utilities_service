from django.shortcuts import render
from django.db.models import F, Q
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerServiceRequest, RequestTracking
from utils.aws_helper import Aws_helper
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerServiceRequestSerializer, RequestTrackingSerializer

# Create your views here.


class CustomerServiceRequestView(APIView): 
    # permission_classes = [IsAuthenticated]
    # JWTAuthentication is handeled in settings already
    def get(self, request):
        try:
            user_id = request.user.id
            user_id = 1 #for your testing otherwise I'll get this Id from token
            address = CustomerServiceRequest.objects.filter(user_id = user_id)
            serializer = CustomerServiceRequestSerializer(address, many = True)
            if serializer.data:
                return Response({
                    "success": True,
                    "message": "Successfully fetched your service requests",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response({
                "success": True,
                "error": False,
                "message": "No complaints till now!",
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e),
                "message": "Failed to retrieve your request."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request): 
        try:
            data = request.data
            user_id = request.user.id
            user_id = 1 #for your testing otherwise I'll get this Id from token
            data['user'] = user_id

            #This will work if I Set the AWS_ACCESS_KEY_ID environment variable 
            # if 'attach_files' in request.FILES:
            #     aws = Aws_helper() 
            #     file_upload_files = aws.upload_s3_bucket("attach_files", request.FILES['attach_files'].name,request.FILES['attach_files'])
            #     attached_file = file_upload_files['s3_key']
            #     data['attached_file'] = attached_file   

            serializer = CustomerServiceRequestSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "error": False,
                    "data": serializer.data,
                    'status': status.HTTP_201_CREATED,
                    'message': "Service request added successfully!"}, status =status.HTTP_200_OK)

            return Response({
                "success": False,
                "errors": serializer.errors,
                'message': "Service Request not created",
                }, status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"success": False,
                            "error": str(e),
                            'message': "Service Request not created"}, status = status.HTTP_400_BAD_REQUEST)


class RequestTrackingView(APIView): 
    permission_classes = [IsAuthenticated]
    # JWTAuthentication is handeled in settings already
    def get(self, request):
        try:
            user_id = request.user.id
            requests = RequestTracking.objects.filter(user_id = user_id)
            serializer = RequestTrackingSerializer(requests, many = True)
            if serializer.data:
                return Response({
                    "success": True,
                    "message": "Successfully fetched your service requests",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response({
                "success": True,
                "error": False,
                "message": "No complaints till now!",
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e),
                "message": "Failed to retrieve your request."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
