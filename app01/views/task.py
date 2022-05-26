import json

from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from templates.utils import bootstrap


class TaskModelForm(ModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "level": widgets.Select(attrs={'class': 'form-control'}),
            "title": widgets.TextInput(attrs={'class': 'form-control'}),
            "detail": widgets.TextInput(attrs={'class': 'form-control'}),
            "user": widgets.Select(attrs={'class': 'form-control'})
        }


@csrf_exempt
def task(request):
    querrset = models.Task.objects.all().order_by("id")
    form = TaskModelForm()
    context = {
        "form": form,
        "quertset": querrset,
    }
    return render(request, 'html/taskmanagement/task.html', context)


@csrf_exempt
def task_add(request):
    print(request.POST)
    # 表单请求校验
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return JsonResponse(data_dict)
    data_dict = {"status": False, "error": form.errors}
    return JsonResponse(data_dict)
