# Generated by Django 4.0 on 2022-05-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_alter_claimdata_mis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimdata',
            name='chassisnumber',
            field=models.CharField(max_length=128, verbose_name='底盘号'),
        ),
        migrations.AlterField(
            model_name='claimdata',
            name='enginenumber',
            field=models.CharField(max_length=128, verbose_name='发动机号'),
        ),
        migrations.AlterField(
            model_name='claimdata',
            name='number_of_parts',
            field=models.CharField(max_length=128, verbose_name='零件号'),
        ),
        migrations.AlterField(
            model_name='claimdata',
            name='productioncode',
            field=models.CharField(max_length=128, verbose_name='生产代码'),
        ),
        migrations.AlterField(
            model_name='claimdata',
            name='subgroupnumber',
            field=models.CharField(max_length=128, verbose_name='子组号'),
        ),
        migrations.AlterField(
            model_name='claimdata',
            name='unitcode',
            field=models.CharField(max_length=64, verbose_name='单位编码'),
        ),
    ]
