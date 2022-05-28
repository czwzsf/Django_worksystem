# Ajax学习

浏览器向网站发送请求时:URL和表单的形式提交

- GET
- POST

特点：这两种请求方式会导致页面刷新

Ajax请求

- 依赖jQuery
- 编写Ajax代码

```javascript
$.ajax({
  url:"发送的地址",
  type:"post",
  data:{
    n1:123,
    n2:456,
  },
  success:function(res){
    console.log(res);
  }
})
```

### GET请求模板

```javascript
    <script type="text/javascript">
        function clickMe() {
            $.ajax({
                url: '/MIS/test/',
                type: "get",
                data: {
                    n1: 123,
                    n2: 456,
                },
                success: function (res) {
                    console.log(res);
                }
            })
        }
    </script>
```

```python
def mis_test(request):
    print(request.GET)
    return HttpResponse("成功了！")

```

### POST请求模板

使用`from django.views.decorators.csrf import csrf_exempt`的`csrf_exempt`来免除`csrf_token`

```python
@csrf_exempt
def mis_test(request):
    print(request.POST)
    return HttpResponse("成功了！")
```

```javascript
    <script type="text/javascript">
        function clickMe() {
            $.ajax({
                url: '/MIS/test/',
                type: "post",
                data: {
                    n1: 123,
                    n2: 456,
                },
                success: function (res) {
                    console.log(res);
                }
            })
        }
    </script>
```

jQuery版本

```javascript
				$(function () {
            //页面框架加载完成之后代码自动执行下面的函数
            bindBtnEvent();
        })

        function bindBtnEvent() {
            $("btn1").click(function () {
                $.ajax({
                    url: '/MIS/test/',
                    type: "post",
                    data: {
                        n1: 123,
                        n2: 456,
                    },
                    success: function (res) {
                        console.log(res);
                    }
                })
            })
        }
```

Ajax请求的返回值一般返回json格式的，在这里我们使用Django中的`JsonResponse`来进行处理

```python
@csrf_exempt
def mis_test(request):
    data_dict = {'status': True, 'data': [11, 22, 33, 44]}
    return JsonResponse(data_dict)
```

在这里可以将input放入到一个form框里面，使代码更加简便化

```javascript
    <form id="form2">
        <label for="txtuser"></label><input id="txtuser" type="text" placeholder="姓名" name="user"/>
        <label for="txtpwd"></label><input id="txtpwd" type="text" placeholder="密码" name="pwd"/>
    </form>
```

```javascript
        function btnBtn2Event() {
            $("#btn2").click(function () {
                $.ajax({
                    url: '/MIS/test/',
                    type: "post",
                    data: $("#form2").serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        console.log(res.data);
                    }
                })
            })
        }

```

`QueryDict: {'user': ['cow'], 'pwd': ['1999']}>`

[![wakatime](https://wakatime.com/badge/user/c636fb10-cd3b-428e-8eea-8d2c6da35177/project/58426bb1-0741-436e-be94-440f69c03737.svg)](https://wakatime.com/badge/user/c636fb10-cd3b-428e-8eea-8d2c6da35177/project/58426bb1-0741-436e-be94-440f69c03737)

### 网页图表生成

- highchart 国外的
- echarts 国内的，百度开源的

```javascript
<script src="{% static 'js/echarts.js' %}"></script>
    <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('m2'));

        // 指定图表的配置项和数据
        var option = {
            title: {
                text: '12MIS'
            },
            tooltip: {},
            legend: {
                data: ['销量']
            },
            xAxis: {
                data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
            },
            yAxis: {},
            series: [
                {
                    name: '销量',
                    type: 'bar',
                    data: [5, 20, 36, 10, 10, 20]
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
```

### 文件上传

#### 基本操作

```html
{% extends 'html/master.html' %}
{% block title %}
    <title>文件上传</title>
{% endblock %}

{% block content %}
    <div class="container">
        <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            <input type="text" name="name">
            <input type="file" name="filename">
            <input type="submit" value="提交">
        </form>
    </div>
{% endblock %}
```

```python
# 请求体中的数据
print(request.POST)  # <QueryDict: {'name': ['czw']}>
# 请求发过来的文件
print(request.FILES)  # <MultiValueDict: {'filename': [<InMemoryUploadedFile: Ajax学习.md (text/markdown)>]}>
return HttpResponse("文件上传成功了")

```

```python
    # 文件读取
  	file_object = request.FILES.get("filename")
    f = open('a1.png', mode="wb")
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
```

### 批量上传excel

https://wakatime.com/@c636fb10-cd3b-428e-8eea-8d2c6da35177/projects/byvtwjqpsv?start=2022-05-22&end=2022-05-28

[![wakatime](https://wakatime.com/badge/user/c636fb10-cd3b-428e-8eea-8d2c6da35177/project/58426bb1-0741-436e-be94-440f69c03737.svg)](https://wakatime.com/badge/user/c636fb10-cd3b-428e-8eea-8d2c6da35177/project/58426bb1-0741-436e-be94-440f69c03737)

