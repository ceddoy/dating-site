from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from clientapp.models import Client


class CreateClientModelSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ("first_name", "last_name", "email", "sex", "avatar", "password")
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', "first_name", "last_name", "sex", "avatar")


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        style={'input_type': 'email'},
        label="Email",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    latitude = serializers.DecimalField(
        label='Широта',
        max_digits=22,
        decimal_places=16,
        required=True
    )

    longitude = serializers.DecimalField(
        label='Долгота',
        max_digits=22,
        decimal_places=16,
        required=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
