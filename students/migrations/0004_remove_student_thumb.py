# Generated by Django 2.1.3 on 2018-11-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20181129_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='thumb',
        ),
    ]
