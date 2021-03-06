# Generated by Django 4.0 on 2022-05-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_delete_servicestationinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productioncode', models.CharField(max_length=32, verbose_name='生产代码')),
                ('enginenumber', models.CharField(max_length=32, verbose_name='发动机号')),
                ('productiondata', models.CharField(max_length=128, verbose_name='生产日期')),
                ('saletime', models.CharField(max_length=128, verbose_name='销售日期')),
                ('chassisnumber', models.CharField(max_length=128, verbose_name='底盘号')),
                ('number_of_failures', models.CharField(max_length=32, verbose_name='故障数量')),
                ('enginemodel', models.CharField(max_length=16, verbose_name='发动机型号')),
                ('shangdaichuname', models.CharField(max_length=32, verbose_name='商代处名称')),
                ('number_of_dealer', models.CharField(max_length=16, verbose_name='经销商代码')),
                ('name_of_dealer', models.CharField(max_length=128, verbose_name='经销商名称')),
                ('cage', models.CharField(max_length=128, verbose_name='驾驶室')),
                ('axle', models.CharField(max_length=128, verbose_name='前桥')),
                ('termianldata', models.CharField(max_length=32, verbose_name='终端日期')),
                ('carmodel', models.CharField(max_length=32, verbose_name='车型')),
                ('terrance', models.CharField(max_length=8, verbose_name='平台')),
                ('technicalroute', models.CharField(max_length=32, verbose_name='技术路线')),
                ('sample_of_vechile', models.CharField(max_length=8, verbose_name='样本车辆')),
                ('province', models.CharField(max_length=16, verbose_name='省份')),
                ('city', models.CharField(max_length=16, verbose_name='城市')),
            ],
        ),
    ]
