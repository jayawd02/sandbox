# Generated by Django 3.1 on 2020-08-06 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200806_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
