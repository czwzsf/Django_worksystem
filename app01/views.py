from django.shortcuts import render, redirect, HttpResponse
from django import forms

# Create your views here.
from django.utils.safestring import mark_safe
from templates.utils import bootstrap
from app01 import models


# 服务站管理
# def depart_list(request):
#     value = request.GET.get('query', '')
#     reset_button = request.GET.get('reset')
#     data_dict = {}
#     page = int(request.GET.get('page', 1))
#     page_size = 20
#     start = (page - 1) * page_size
#     end = page * page_size
#
#     # 页码
#     page_str_list = []
#     page_number = models.DepartmentInfo.objects.filter(**data_dict).count()
#     total_page_count, div = divmod(page_number, page_size)
#     if div:
#         total_page_count = total_page_count + 1
#     for i in range(page, page + 6):
#         ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
#         page_str_list.append(ele)
#     page_string = mark_safe("".join(page_str_list))
#     if value:
#         data_dict['title'] = value
#         queryset = models.DepartmentInfo.objects.filter(**data_dict)[start:end]
#     else:
#         queryset = models.DepartmentInfo.objects.all()[start:end]
#     if reset_button == 0:
#         queryset = models.DepartmentInfo.objects.all()[start:end]
#     return render(request, 'html/Depart/depart_list.html', {"queryset": queryset, "page_string": page_string})
#
#
# def servicestation_list(request):
#     servicestation_list_info = models.ServicestationInfo.objects.all()
#     return render(request, 'html/Depart/servicestation.html', {"servicestation_list_info": servicestation_list_info})
#
#
# def depart_add(request):
#     """添加部门"""
#     if request.method == 'GET':
#         return render(request, 'html/Depart/depart_add.html')
#     # 获取用户提交出来的结果,将其存入到数据库里面
#     elif request.method == 'POST':
#         depart_name = request.POST.get("depart_name")
#         # 保存到数据库
#         models.DepartmentInfo.objects.create(title=depart_name)
#         # 重定向回到部门页面
#         return redirect("/depart/list/")
#
#
# def depart_delete(request):
#     nid = request.GET.get('nid')
#     models.DepartmentInfo.objects.filter(id=nid).delete()
#     return redirect("/depart/list/")
#
#
# def depart_edit(request, nid):
#     """修改部门信息"""
#     if request.method == 'GET':
#         row_object = models.DepartmentInfo.objects.filter(id=nid).first()
#         return render(request, 'html/Depart/depart_edit.html', {'row_object': row_object})
#     depart_edit_name = request.POST.get("depart_edit")
#     models.DepartmentInfo.objects.filter(id=nid).update(title=depart_edit_name)
#     return redirect("/depart/list/")


# 用户管理
def user_list(request):
    """用户管理 - 列表"""
    # 获取用户数据
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


# 管理员管理
def admin_list(request):
    """管理员列表"""

    queryset = models.Admin.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'html/admin/admin_list.html', context)


class LoginForm(bootstrap.BootStrapForm):
    name = forms.CharField(label='username', widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control"}),
                               required=True)


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'html/User/user_login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if not user_object:  # 查看是否找到了用户模型
            form.add_error('password', 'password or username is error')
            return render(request, 'html/User/user_login.html', {'form': form})
        # 用户名与密码正确
        # 用户生成随机字符串；写到用户浏览器的cookie中去
        return redirect('/user/list/')
    else:
        return render(request, 'html/User/user_login.html', {'form': form})
