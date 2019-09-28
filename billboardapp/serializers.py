from rest_framework import serializers
from billboardapp.models import Product, User



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


class ProductDetailSerializers(serializers.ModelSerializer):
    # пользователь который создает автоматически прикрепляется к записи
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'user', 'date_pub')


class ProductListSerializers(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'date_pub')