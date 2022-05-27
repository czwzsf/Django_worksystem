from django.shortcuts import render, redirect

from django.forms import ModelForm
from django.forms import widgets
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models


def upload_list(request):
    if request.method == "GET":
        return render(request, 'html/upload/upload_list.html')
    # 请求体中的数据
    file_object = request.FILES.get("filename")
    f = open('a1.png', mode="wb")
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("文件上传成功了")
