from django.urls import path
from .views import user_login, signupview

urlpatterns = [
    path('', user_login, name='login'),
    path('signup/', signupview, name='signup'),
]