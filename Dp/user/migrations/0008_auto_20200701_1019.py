# Generated by Django 3.0.6 on 2020-07-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200629_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=111),
        ),
    ]
