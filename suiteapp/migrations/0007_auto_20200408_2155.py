# Generated by Django 3.0 on 2020-04-08 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0006_auto_20200408_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='faculty',
            field=models.ForeignKey(blank=True, default='null', null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Faculty'),
        ),
    ]
