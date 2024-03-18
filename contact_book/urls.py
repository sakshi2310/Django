"""
URL configuration for contact_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from contact_app.views import *


urlpatterns = [
    path('',login),
    path('register/',register),
    path('login/',login),
    # path('index/',index),
    path('logout/',logout),
    path('add_contact/',add_contact),
    path('view_contact/',view_contact),
    path('edit_data/<int:edit_id>',edit_data),
    path('del_data/<int:del_id>',del_data),
    path('edit_user/',edit_user),
    path('admin_confirmation/',admin_confirmation),
    path('header/',header),
    path('admin/', admin.site.urls),
]

