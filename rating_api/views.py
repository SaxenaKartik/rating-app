from django.shortcuts import render
# from rest_framework import viewsets
from rating_api import models
from rating_api import serializers
from django.views import View
from django.http import HttpResponse
from .models import MyUser, Product
from rest_framework.renderers import JSONRenderer

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     """ Handle creating and updating users"""
#
#     serializer_class = serializers.UserSerializer
#     queryset = models.MyUser.objects.all()
#
#
# class ProductViewSet(viewsets.ModelViewSet):
#     """ Handle creating and updating products"""
#
#     serializer_class = serializers.ProductSerializer
#     queryset = models.Product.objects.all()
class login(View):
    serializer_class = serializers.UserSerializer
    renderer_classes = ['TemplateHTMLRenderer']
    template_name = 'login.html'

    def get(self, request):
        model = MyUser.objects.get.all()
        serializer = ModelSerializer(model)
        return Response({'serializer': serializer, 'model': model})

    def post(self, request):
        pass

class signup(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

class product(View):
    def get(self, request):
        pass

class rate(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
