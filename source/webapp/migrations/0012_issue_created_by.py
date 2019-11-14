# Generated by Django 2.2.5 on 2019-11-07 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0011_auto_20191014_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_by',
            field=models.ForeignKey(default=webapp.models.get_admin, on_delete=django.db.models.deletion.PROTECT, related_name='issues', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]
