from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

__all__ = ['LoginView', 'LogoutView']

class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        pwd = request.data.get('password')
        user = User.objects.filter(username=username, passwd=pwd).first()

        if not user:
            return Response({'code':403, 'error': '用户名或密码错误'})