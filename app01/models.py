from django.db import models


# Create your models here.
class DepartmentInfo(models.Model):
    """部门名称"""
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """用户信息"""
    name = models.CharField(max_length=32, verbose_name='姓名')
    password = models.CharField(max_length=128, verbose_name='密码')
    age = models.IntegerField(default=2, null=True,
                              blank=True, verbose_name='年龄')
    # size = models.IntegerField(default=2)
    email = models.CharField(max_length=128, null=True,
                             blank=True, verbose_name='邮箱')
    depart = models.ForeignKey(to="DepartmentInfo", on_delete=models.CASCADE, to_field="id", default=1,
                               verbose_name='部门')


class ServicestationInfo(models.Model):
    station_id = models.CharField(max_length=128)
    station_name = models.CharField(max_length=128)
    station_address = models.CharField(max_length=128)


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=128)
    email = models.CharField(
        verbose_name="邮箱", max_length=128, null=True, blank=True)
