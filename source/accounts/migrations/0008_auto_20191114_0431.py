# Generated by Django 2.2.5 on 2019-11-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191108_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End date'),
        ),
    ]