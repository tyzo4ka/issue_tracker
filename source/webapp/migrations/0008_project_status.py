# Generated by Django 2.2.5 on 2019-10-10 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20191010_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.Status'),
        ),
    ]
