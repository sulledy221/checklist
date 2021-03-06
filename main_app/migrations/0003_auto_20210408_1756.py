# Generated by Django 3.1.7 on 2021-04-08 17:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_checklist_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('relax', models.CharField(max_length=20)),
            ],
            managers=[
                ('vacation', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='vacation',
            field=models.ManyToManyField(to='main_app.Vacation'),
        ),
    ]
