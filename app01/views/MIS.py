from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app01 import models


def MIS(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')
    return render(request, 'html/MIS/MIS.html')


@csrf_exempt
def mis_test(request):
    print(request.POST)
    data_dict = {'status': True, 'data': [11, 22, 33, 44]}
    return JsonResponse(data_dict)


def mis_chart(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')
    return render(request, 'html/MIS/mis_chart.html')


def mis_chart_bar(request):
    # 构造柱状图
    legend = ['chenzhewei', 'hll']
    series_list = [
        {
            "name": "chenzhewei",
            "type": 'bar',
            "data": [1, 2, 3, 4, 5, 6]
        },
        {
            "name": "hll",
            "type": 'bar',
            "data": [2, 3, 4, 5, 6, 7]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }
    return JsonResponse(result)


def mis_chart_line(request):
    queryset = models.Mis.objects.all()
    legend = ["3MIS", "6MIS", "12MIS"]
    x_axis = []
    data_3mis = []
    data_6mis = []
    data_12mis = []
    title = queryset[0].name_of_parts + "MIS趋势图"
    for form in queryset:
        # 将x轴的数据写入到数组内
        x_axis.append(form.date)
        data_3mis.append(float(form.mis_3))
        data_6mis.append(float(form.mis_6))
        data_12mis.append(float(form.mis_12))
    series_list = [
        {
            "name": "3MIS",
            "type": "line",
            "data": data_3mis,
            "stack": "Total",
        },
        {
            "name": "6MIS",
            "type": "line",
            "data": data_6mis,
            "stack": "Total",
        },
        {
            "name": "12MIS",
            "type": "line",
            "data": data_12mis,
            "stack": "Total",
        },
    ]
    result = {
        "status": True,
        "data": {
            "title": title,
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }
    return JsonResponse(result)
