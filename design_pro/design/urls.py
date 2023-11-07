from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.ApplicationsView.as_view(), name='base'),
    path('login/', views.login, name='login'),
    path('logged_out/', views.logout, name='logged_out'),
    path('my_request/', views.MyRequestView.as_view(), name='my_request'),
    path('get_request/', views.GetRequest.as_view(), name='get_request'),
    path('request/<int:pk>/delete/', views.RequestDelete.as_view(), name='request_delete'),
    path('change_category/', views.ChangeCategory.as_view(), name='change_category'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('create_category/', views.CreateCategory.as_view(), name='category_create'),

]



