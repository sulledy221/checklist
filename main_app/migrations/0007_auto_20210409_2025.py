# Generated by Django 3.1.7 on 2021-04-09 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210409_2018'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='vacation',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='relax',
        ),
    ]