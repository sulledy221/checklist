# Generated by Django 3.1.7 on 2021-04-09 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_relax_checklist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relax',
            options={'ordering': ['-date']},
        ),
    ]