from django.urls import path
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
     path('test/', views.get_data),
     path('register/', views.register),# register to the website 
     path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),# log in
]