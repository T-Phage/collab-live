# Generated by Django 3.0 on 2020-05-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0031_auto_20200501_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folder_name',
            field=models.CharField(max_length=255),
        ),
    ]