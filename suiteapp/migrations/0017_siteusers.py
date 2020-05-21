# Generated by Django 3.0 on 2020-04-12 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suiteapp', '0016_delete_site_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Role')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suiteapp.Site')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
