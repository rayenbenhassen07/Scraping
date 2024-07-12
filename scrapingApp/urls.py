from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
  

    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),

    path('add_website/', views.add_website, name='add_website'),
    path('delete_website/<int:id>/', views.delete_website, name='delete_website'),
    path('edit_website/<int:id>/', views.edit_website, name='edit_website'),
    
    path('run_website/<int:id>/', views.run_website, name='run_website'),
    

]