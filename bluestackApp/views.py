from django.shortcuts import render
from rest_condition import Or, And
import datetime
from .serializers import(
    UserSignupSerializer,
    UserLoginSerializer, 
    EmployeeDetailSerializer, 
    EmployeeUpdateSerializer,
    EmployeeDeleteSerializer,
    RoomCreateSerializer,
    RoomDetailSerializer, 
    RoomUpdateSerializer,
    RoomDeleteSerializer
    
    )
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .models import User, ConfRoom
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status, serializers, authentication
from rest_framework.authtoken.models import Token
from bluestackApp.permission import AdminPermission, IsEnggManager, IsOfficeManager, IsEmployee

class UserSignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        }) 

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token= Token.objects.get_or_create(user=user)
            response = {"data": {"message":"You have logged in successfully.",
													  "token": str(token), 
										},
								"status": 200,}
            return Response(response, status=status.HTTP_200_OK)
        else:
            error_data = serializer.errors
            return Response(data=error_data)

class EmpoloyeeCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = (Or(IsEnggManager,AdminPermission),)

class EmployeeDetailView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = (Or(IsEnggManager,AdminPermission,IsEmployee),)

class EmployeeUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeUpdateSerializer
    permission_classes = (Or(And(IsAuthenticated,IsEnggManager),AdminPermission),)

class EmployeeDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeDeleteSerializer
    permission_classes = [IsAuthenticated,AdminPermission]


class RoomCreateView(CreateAPIView):
    queryset = ConfRoom.objects.all()
    serializer_class = RoomCreateSerializer
    permission_classes = (Or(And(IsAuthenticated,IsOfficeManager),AdminPermission),)

class RoomDetailView(ListAPIView):
    queryset = ConfRoom.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [Or(And(IsAuthenticated,IsOfficeManager),And(IsAuthenticated,IsEmployee),AdminPermission),]

class RoomUpdateView(UpdateAPIView):
    queryset = ConfRoom.objects.all()
    serializer_class = RoomUpdateSerializer
    permission_classes = [Or(And(IsAuthenticated,IsOfficeManager),AdminPermission),]

class RoomDeleteView(DestroyAPIView):
    queryset = ConfRoom.objects.all()
    serializer_class = RoomDeleteSerializer
    permission_classes = [IsAuthenticated,AdminPermission]



