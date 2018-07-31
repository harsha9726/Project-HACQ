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

urlpatterns = [
    path('',views.index, name='index'),
    path('Criteria2_fill',views.Criteria2_fill, name='Criteria2_fill'),
    path('Criteria4_fill',views.Criteria4_fill, name='Criteria4_fill'),
    path('Criteria6_fill',views.Criteria6_fill, name='Criteria6_fill'),
    path('Criteria7_fill',views.Criteria7_fill, name='Criteria7_fill'),
    path('institute_fill/',views.institute_fill, name='institute_fill'),
    path('admin/', admin.site.urls, name='admin'),
    path('details/',views.form_details, name='details'),
    path('save/', views.save_institution_details, name='save_institution_details'),
]
