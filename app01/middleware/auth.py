from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Login_validation(MiddlewareMixin):
    """实现登入校验的工作"""

    def process_requset(self, request):
        # 读取当前访问的用户的session信息，如果能读取到，就可以登入
        if request.path_info in ["/login/"]:  # 将登入界面排除到中间件判定外，免得重复请求登入
            return None
        info_dict = request.session.get("info")
        if info_dict:
            return None  # 返回None则请求继续向前传递
        return redirect('/login/')  # 没有登入过的话，回到登入界面
