# Generated by Django 3.0 on 2020-04-07 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0003_remove_folder_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Department'),
        ),
    ]