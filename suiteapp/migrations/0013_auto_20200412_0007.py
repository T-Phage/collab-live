# Generated by Django 3.0 on 2020-04-12 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0012_auto_20200411_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_members',
            name='members',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='site_members',
            name='role',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Role'),
        ),
    ]
