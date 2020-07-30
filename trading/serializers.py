from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Stock, StockFolioUser, StockPortfolio



class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'



class StockFolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockFolioUser
        fields = '__all__'
        # user = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return StockFolioUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance



class StockPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPortfolio
        fields = '__all__'
        owner = serializers.ReadOnlyField(source='owner.username')



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

