from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.ApplicationsView.as_view(), name='base'),
    path('my_request/', views.MyRequestView.as_view(), name='my_request'),
    path('get_request/', views.GetRequest.as_view(), name='get_request'),


]



