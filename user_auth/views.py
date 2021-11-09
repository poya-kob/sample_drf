from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .serializers import LoginSerializer


class UserAuth(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_auth/login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        username = self.request.data['username']
        password = self.request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
