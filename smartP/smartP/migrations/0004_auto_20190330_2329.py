# Generated by Django 2.1.7 on 2019-03-30 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartP', '0003_auto_20190321_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteparkinglot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
