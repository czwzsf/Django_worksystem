"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    # path('depart/list/', views.depart_list),
    # path('servicestaion/', views.servicestation_list),
    # path('depart/add/', views.depart_add),
    # path('depart/delete/', views.depart_delete),  # 就算没有编辑网络页面，也需要在urls里面注册网址
    # path('depart/<int:nid>/edit/', views.depart_edit),
    # 用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/addmodel/', views.user_addmodel),
    path('user/<int:nid>/edit', views.user_edit),
    path('user/delete/', views.user_delete),
    # 管理员管理
    path('admin/list/', views.admin_list),
    # user_login
    path('login/', views.login),
    path('logout/',views.logout)
]
