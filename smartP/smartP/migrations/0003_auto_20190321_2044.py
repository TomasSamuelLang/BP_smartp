# Generated by Django 2.1.7 on 2019-03-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartP', '0002_auto_20190318_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]