# Generated by Django 4.2.16 on 2024-11-09 07:27

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_referral_user_leagth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='scrach_list',
        ),
        migrations.AddField(
            model_name='user',
            name='scrach_list',
            field=django_mysql.models.ListTextField(models.IntegerField(), blank=True, null=True, size=100),
        ),
    ]
