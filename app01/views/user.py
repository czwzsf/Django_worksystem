import json

from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from templates.utils import bootstrap


def user_list(request):
    """用户管理 - 列表"""
    # 获取用户数据
    # 检查用户是否已经登入
    # 用户发来请求，检查cookies随机字符串，查看session中有没有相对应的
    info = request.session.get("info")
    if not info:
        return redirect('/login/')
    user_list_info = models.UserInfo.objects.all()
    return render(request, 'html/User/user_list.html', {"user_list_info": user_list_info})


def user_add(request):
    if request.method == 'GET':
        context = {
            "depart_list": models.DepartmentInfo.objects.all(),
        }
        return render(request, 'html/User/user_add.html', context)
    # 获取用户提交的数据
    username = request.POST.get('user_name')
    depart_id = request.POST.get('depart_name')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    email = request.POST.get('email')
    if bool(password):
        if password == repassword:
            models.UserInfo.objects.create(name=username, password=password, depart_id=depart_id, email=email)
            return redirect('/user/list')
        else:
            return HttpResponse("两次密码不一致，请重新输入！！！！")
    else:
        return HttpResponse("请按要求输入内容")


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', 'depart', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'placeholder': field.label}


def user_addmodel(request):
    """添加用户，但是是ModelForm版本"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'html/User/user_addmodel.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    else:
        return render(request, 'html/User/user_addmodel.html', {'form': form})


def user_edit(request, nid):
    """编辑"""
    if request.method == 'GET':
        row_object = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        return render(request, 'html/User/user_edit.html', {'form': form})
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list')

    return render(request, 'html/User/user_edit.html', {'form': form})


def user_delete(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
