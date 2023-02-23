from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

common_urls = [
    path('login', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterAPIView.as_view(), name='register_user'),
    #path('register', RegisterView.as_view(), name='auth_register'),

    # path('login', UserLoginAPIView.as_view(), name='login'),
    # path('refresh', RefreshTokenAPIView.as_view(), name='refresh_token'),


]

urlpatterns = common_urls
