from rest_framework import serializers
from rating_api import models

class UserSerializer(serializers.ModelSerializer):
    """Serializes fields for User Model"""
    class Meta :
        model = models.MyUser
        fields = ('username', 'password')
        extra_kwargs = {
            'password' :{
                'style' : {'input_type' : 'password'}
            }
        }
    
class ProductSerializer(serializers.ModelSerializer):
    """Serializes fields for Product Model"""
    class Meta :
        model = models.Product
        fields = ('name', 'price', 'rating')
