from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

from base.models import Profile

def index(req):
    return JsonResponse('hello', safe=False)


@api_view(['GET'])
def get_data(request):
    if request.method == 'GET':
        return JsonResponse({"test":"test"} , safe=False)
    

@api_view(["POST"])
def register(request):
    Username = request.data["username"]
    Password = request.data["password"]
    Email = request.data["email"]
    First_name = request.data["first_name"]
    Last_name = request.data["last_name"]
    print(Username, Password, Email,)
    user = User.objects.create_user(
        username=Username, password=Password, email=Email,first_name= First_name, last_name= Last_name)
    return Response({"first name": First_name, "last name": Last_name})


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # classmethod (static method) method we can use with out creating an object
    @classmethod
    def get_token(cls, user):
        # super -> the class we inherit
        token = super().get_token(user)
        # select one row from Profile table (where user = given user)

        # from here it's our code
        pro = Profile.objects.get(user=user)
        print(pro)
        # our code done
        # ...

        return token
    
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer