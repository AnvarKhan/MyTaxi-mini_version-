from rest_framework import serializers
from driver.models import User, Client, Driver, Order


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserREGSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            'firstname',
            'lastname',
            'username',
            'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user
