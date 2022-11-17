from django.contrib.auth import login
from django.contrib.auth.models import User

#
# def user_login(func):
#     def inner(request):
#         if request.user.is_authenticated:
#             func(request)
#         else:
#