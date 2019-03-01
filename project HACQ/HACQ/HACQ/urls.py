"""HACQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from CriteriaForm import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('Criteria1_fill', views.Criteria1_fill, name='Criteria1_fill'),
    path('Criteria2_fill', views.Criteria2_fill, name='Criteria2_fill'),
    path('Criteria3_fill', views.Criteria3_fill, name='Criteria3_fill'),
    path('Criteria4_fill', views.Criteria4_fill, name='Criteria4_fill'),
    path('Criteria5_fill', views.Criteria5_fill, name='Criteria5_fill'),
    path('Criteria6_fill', views.Criteria6_fill, name='Criteria6_fill'),
    path('Criteria7_fill', views.Criteria7_fill, name='Criteria7_fill'),
    path('institute_fill/', views.institute_fill, name='institute_fill'),
    path('admin/', admin.site.urls, name='admin'),
    path('details/', views.form_details, name='details'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='form/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='form/logout.html'), name='logout'),

]
