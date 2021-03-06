# Generated by Django 4.0 on 2022-05-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_alter_task_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_parts', models.CharField(max_length=128, verbose_name='零部件名称')),
                ('mis_3', models.CharField(max_length=64, verbose_name='3MIS')),
                ('mis_6', models.CharField(max_length=64, verbose_name='6MIS')),
                ('mis_12', models.CharField(max_length=64, verbose_name='12MIS')),
                ('date', models.CharField(max_length=64, verbose_name='日期')),
            ],
        ),
    ]
