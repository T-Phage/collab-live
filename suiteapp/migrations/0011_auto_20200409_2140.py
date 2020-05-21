# Generated by Django 3.0 on 2020-04-09 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0010_auto_20200409_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Department'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Faculty'),
        ),
    ]
