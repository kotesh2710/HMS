from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin_login/', views.Login, name='admin_login'),
    path('logout/', views.logout_admin, name='logout_admin'),
    path('index/', views.index, name='dashboard'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('delete_doctor(?P<int:pid>)/', views.Delete_Doctor, name='delete_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor')



]
