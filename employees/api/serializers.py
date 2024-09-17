from rest_framework import serializers
from django.contrib.auth import authenticate
from ..models import Employee, Product, ListOfProduct
from django.contrib.auth.password_validation import validate_password

class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = Employee
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'job_title', 'date_of_birth', 'hire_date', 'salary']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employee.objects.create_user(**validated_data)
        return user

class EmployeeLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ListOfProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ListOfProduct
        fields = ['id', 'name', 'employee', 'products', 'date_created']
        read_only_fields = ['employee']