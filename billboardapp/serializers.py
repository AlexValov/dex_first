from rest_framework import serializers
from billboardapp.models import User, Product


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data.get('email')
        user.set_password(password)
        user.save()
        return user


class ProductDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'user', 'date_pub')

        extra_kwargs = {
            'name': {'max_length': 50, 'required': True},
            'description': {'max_length': 500, 'required': True},
            'image': {'max_length': 15, 'allow_empty_file': False},
            'price': {'min_value': 0, 'required': True},
            'date_pub': {'default_timezone': None}
        }


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'date_pub')
