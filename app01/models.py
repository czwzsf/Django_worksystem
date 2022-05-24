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

    def __str__(self):
        return self.name


# class ServicestationInfo(models.Model):
#     station_id = models.CharField(max_length=128)
#     station_name = models.CharField(max_length=128)
#     station_address = models.CharField(max_length=128)
#

class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=128)
    email = models.CharField(
        verbose_name="邮箱", max_length=128, null=True, blank=True)


class salesdata(models.Model):
    """销售数据"""
    productioncode = models.CharField(verbose_name="生产代码", max_length=256)
    enginenumber = models.CharField(verbose_name="发动机号", max_length=256)
    productiondata = models.CharField(verbose_name="生产日期", max_length=256)
    saletime = models.CharField(verbose_name="销售日期", max_length=256)
    chassisnumber = models.CharField(verbose_name="底盘号", max_length=256)
    number_of_failures = models.CharField(verbose_name="故障数量", max_length=8)
    enginemodel = models.CharField(verbose_name="发动机型号", max_length=128)
    shangdaichuname = models.CharField(verbose_name="商代处名称", max_length=256)
    number_of_dealer = models.CharField(verbose_name="经销商代码", max_length=16)
    name_of_dealer = models.CharField(verbose_name="经销商名称", max_length=256)
    cage = models.CharField(verbose_name="驾驶室", max_length=256)
    # axle = models.CharField(verbose_name="前桥", max_length=256)
    # termianldata = models.CharField(verbose_name="终端日期", max_length=32)
    carmodel = models.CharField(verbose_name="车型", max_length=32)
    terrance = models.CharField(verbose_name="平台", max_length=32)
    technicalroute = models.CharField(verbose_name="技术路线", max_length=32)
    sample_of_vechile = models.CharField(verbose_name="样本车辆", max_length=32)
    province = models.CharField(verbose_name="省份", max_length=16)
    city = models.CharField(verbose_name="城市", max_length=16)


class claimdata(models.Model):
    name_of_parts = models.CharField(verbose_name="零件名称", max_length=128)
    chassisnumber = models.CharField(verbose_name="底盘号", max_length=128)
    enginenumber = models.CharField(verbose_name="发动机号", max_length=128)
    subgroupnumber = models.CharField(verbose_name="子组号", max_length=128)
    number_of_parts = models.CharField(verbose_name="零件号", max_length=128)
    productioncode = models.CharField(verbose_name="生产代码", max_length=128)
    productiondata = models.CharField(verbose_name="生产日期", max_length=128)
    saletime = models.CharField(verbose_name="销售日期", max_length=128)
    claimtime = models.CharField(verbose_name="索赔日期", max_length=128)
    moneyclaim = models.CharField(verbose_name="索赔金额", max_length=128)
    materialmoney = models.CharField(verbose_name="材料费", max_length=128)
    mis = models.CharField(verbose_name="MIS", max_length=32)
    unitcode = models.CharField(verbose_name="单位编码", max_length=64)
    providercode = models.CharField(verbose_name="供应商代码", max_length=32)
    providername = models.CharField(verbose_name="供应商名称", max_length=256)
    enginemodel = models.CharField(verbose_name="发动机型号", max_length=128)
    drivendistance = models.CharField(verbose_name="行驶里程", max_length=256)
    Faultdescription = models.CharField(verbose_name="故障描述", max_length=256)
    reason = models.CharField(verbose_name="原因分析", max_length=256)
    errorcode = models.CharField(verbose_name="故障代码", max_length=32)
    unitname = models.CharField(verbose_name="单位名称", max_length=256)
    claimnumber = models.CharField(verbose_name="索赔单号", max_length=128)
    servicestationcode = models.CharField(verbose_name="服务站代码", max_length=128)
    servicestationname = models.CharField(verbose_name="服务站名称", max_length=256)
    cage = models.CharField(verbose_name="驾驶室", max_length=256)
    carmodel = models.CharField(verbose_name="车型", max_length=32)
    terrance = models.CharField(verbose_name="平台", max_length=32)
    technicalroute = models.CharField(verbose_name="技术路线", max_length=32)
    sample_of_vechile = models.CharField(verbose_name="样本车辆", max_length=32)
    productmonth = models.CharField(verbose_name="生产月", max_length=32)
    sortedprovidername = models.CharField(verbose_name="整理后的供应商名称", max_length=256)
    sortedprovidercode = models.CharField(verbose_name="整理后的供应商代码", max_length=32)
    sortedname_of_parts = models.CharField(verbose_name="整理后的零件名称", max_length=128)


class Task(models.Model):
    """项目管理"""
    level_choices = (
        (1, "紧急"),
        (2, "临时"),
        (3, "重要"),
    )
    level = models.SmallIntegerField(verbose_name="任务级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="任务标题", max_length=64)
    detail = models.TextField(verbose_name="任务详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="UserInfo", on_delete=models.CASCADE)
