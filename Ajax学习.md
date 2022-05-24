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

