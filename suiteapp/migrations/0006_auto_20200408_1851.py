# Generated by Django 3.0 on 2020-04-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0005_file_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Faculty'),
        ),
        migrations.AlterField(
            model_name='file',
            name='department',
            field=models.ForeignKey(blank=True, default='null', null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Department'),
        ),
    ]