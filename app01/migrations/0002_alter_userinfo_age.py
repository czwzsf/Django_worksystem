# Generated by Django 4.0 on 2022-04-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]