from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from bluestackApp.models import User
from django.contrib.auth import authenticate, login

class UserSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['user_type','email', 'mobileNumber', 'password', 'username','firstName','lastName','team','position']

    def create(self, validate_data):
        user = User(mobileNumber=validate_data['mobileNumber'],
        username=validate_data['username'],
        email=validate_data['email'],
        user_type=validate_data['user_type'],
        firstName = validate_data['firstName'],
        lastName = validate_data['lastName'],
        team = validate_data['team'],
        position = validate_data['position'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['email','password']
    # Field level serialization

    def validate_email(self, email):
        if not User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("User does not exists. You need to  signup.")
        return email
    # Globally objcet validation using serializer
    
    def validate(self, validate_data):
        email = validate_data.get('email')
        password = validate_data.get('password')
        
        if email and password:
            user_obj = User.objects.get(email__iexact=email)
            username = user_obj.username
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or Password.")
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
        validate_data["user"] = user
        return validate_data

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ['id','user_type','email','firstName','lastName','team','position']

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User 
        fields = ['id','user_type','email','firstName','lastName','team','position']