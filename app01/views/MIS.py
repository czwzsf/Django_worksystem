from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


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
