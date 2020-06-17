from django.urls import path,include
from rating_api import views as app_views
from django.contrib.auth import views
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('user', views.UserViewSet)
# router.register('product', views.ProductViewSet)

urlpatterns = [
    path('login/',views.LoginView.as_view()),
    path('signup/', app_views.signup),
    path('product/', app_views.product),
    path('rate/', app_views.rate)
]
