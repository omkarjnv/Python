# Generated by Django 2.1.3 on 2018-12-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_student_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='name',
            field=models.CharField(default='nitish123', max_length=10),
        ),
        migrations.AddField(
            model_name='reply',
            name='name',
            field=models.CharField(default='nitish123', max_length=10),
        ),
    ]