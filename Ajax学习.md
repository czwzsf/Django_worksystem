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

