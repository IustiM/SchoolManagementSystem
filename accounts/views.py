from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import NewUser
from .serializers import NewUserSerializer, CustomAccountManagerSerializer


#
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {'form': form})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, 'Invalid username or password')
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})
#
# @login_required
# def logout(request):
#     return redirect('home')
#
#
# def home(request):
#     # response = HttpResponse('merge')
#     # return response
#     return render(request, 'accounts/home.html')
#
# def profile(request):
#     return render(request, 'accounts/profile.html')

class home(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name='accounts/home.html'
    def get(self, request):
        # return render(request, 'accounts/home.html')
        return Response()

class login(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'accounts/login.html'
    def get(self, request):
        return Response()

class logout(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'accounts/logout.html'
    def get(self, request):
        return Response()

class profile(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'accounts/profile.html'
    def get(self, request):
        return Response()



class NewUserList(APIView):

    def get(self, request, format=None):
        new_users = NewUser.objects.all()
        serializer = NewUserSerializer(new_users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewUserDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(NewUser, pk=pk)

    def get(self, request, pk, format=None):
        new_user = self.get_object(pk)
        serializer = NewUserSerializer(new_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        new_user = self.get_object(pk)
        serializer = NewUserSerializer(new_user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        new_user = self.get_object(pk)
        new_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomAccountManagerList(APIView):

    def get(self, request, format=None):
        managers = NewUser.objects.all()
        serializer = CustomAccountManagerSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomAccountManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAccountManagerDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(CustomAccountManagerDetail, pk=pk)

    def get(self, request, pk, format=None):
        manager = self.get_object(pk)
        serializer = CustomAccountManagerSerializer(manager.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        manager = self.get_object(pk)
        serializer = CustomAccountManagerSerializer(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        manager = self.get_object(pk)
        manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# <!--                <li><a href="{% url 'students/students' %}">Students</a></li>-->
