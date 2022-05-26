import json

from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from templates.utils import bootstrap
from app01.views.user import UserModelForm


def admin_list(request):
    """管理员列表"""

    queryset = models.Admin.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'html/admin/admin_list.html', context)


class LoginForm(UserModelForm):
    # name = forms.CharField(label='username', widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    # password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control"}),
    #                            required=True)
    # image_code = forms.CharField(label='image_code', widget=forms.TextInput(), required=True)
    class Meta:
        model = models.UserInfo
        fields = {"name", "password"}


# class LoginForm(bootstrap.BootStrapModelForm):
#     # name = forms.CharField(label='username', widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
#     # password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control"}),
#     #                            required=True)
#     # image_code = forms.CharField(label='image_code', widget=forms.TextInput(), required=True)
#     class Meta:
#         model = models.UserInfo
#         fields = {"name", "password"}
#

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'html/User/user_login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 在这里使用pop的原因是因为我们创建的
        # user_input_code = form.cleaned_data.pop('image_code')
        # image_code = request.session.get('image_code', '')
        # if image_code.upper() != user_input_code.upper():
        #     form.add_error('image_code', '验证码错误或者过期，请注意验证码的时间限制为60s')
        #     return render(request, 'html/User/user_login.html', {'form': form})
        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if not user_object:  # 查看是否找到了用户模型
            form.add_error('password', 'password or username is error')
            return render(request, 'html/User/user_login.html', {'form': form})
        # 用户名与密码正确
        # 用户生成随机字符串；写到用户浏览器的cookie中去
        # 将cookies写入
        request.session["info"] = {'id': user_object.id, 'name': user_object.name}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/user/list/')
    else:
        return render(request, 'html/User/user_login.html', {'form': form})


def logout(request):
    """注销"""
    request.session.clear()  # 清除掉当前用户的session信息
    return redirect('/login/')
