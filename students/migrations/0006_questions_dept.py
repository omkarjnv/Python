# Generated by Django 2.1.3 on 2018-12-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20181202_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='Dept',
            field=models.CharField(default='CSE', max_length=10),
        ),
    ]
