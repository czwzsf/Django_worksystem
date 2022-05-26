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
from django.urls import path
from app01 import views
from app01.views import user, admin, MIS, task

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    # path('depart/list/', views.depart_list),
    # path('servicestaion/', views.servicestation_list),
    # path('depart/add/', views.depart_add),
    # path('depart/delete/', views.depart_delete),  # 就算没有编辑网络页面，也需要在urls里面注册网址
    # path('depart/<int:nid>/edit/', views.depart_edit),
    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/addmodel/', user.user_addmodel),
    path('user/<int:nid>/edit', user.user_edit),
    path('user/delete/', user.user_delete),
    # 管理员管理
    path('admin/list/', admin.admin_list),
    # user_login
    path('login/', admin.login),
    path('logout/', admin.logout),
    # MIS计算与文件上传功能
    path('MIS/', MIS.MIS),
    path('MIS/test/', MIS.mis_test),
    path('MIS/chart/', MIS.mis_chart),
    path('MIS/chart/bar', MIS.mis_chart_bar),
    # 任务管理
    path('task/', task.task),
    path('task/add/', task.task_add),
]
