import json

from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from templates.utils import bootstrap


def MIS(request):
    return render(request, 'html/MIS/MIS.html')


@csrf_exempt
def mis_test(request):
    print(request.POST)
    data_dict = {'status': True, 'data': [11, 22, 33, 44]}
    return JsonResponse(data_dict)


def mis_chart(request):
    return render(request, 'html/MIS/mis_chart.html')


def mis_chart_bar(request):
    # 构造柱状图
    return None
