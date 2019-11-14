# Generated by Django 2.2.5 on 2019-11-07 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0012_issue_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='assigned_to',
            field=models.ForeignKey(default=webapp.models.get_admin, on_delete=django.db.models.deletion.PROTECT, related_name='issues_assigned', to=settings.AUTH_USER_MODEL, verbose_name='Assigned to'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created_by',
            field=models.ForeignKey(default=webapp.models.get_admin, on_delete=django.db.models.deletion.PROTECT, related_name='issues_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]