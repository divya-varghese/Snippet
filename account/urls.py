from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # fetching access and refresh token from simpleJwt service
    # reference 
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

    # pass valid email and pasword for the response
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # pass refresh token for new access toekens
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]