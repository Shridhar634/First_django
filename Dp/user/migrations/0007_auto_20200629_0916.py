# Generated by Django 3.0.6 on 2020-06-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200629_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='user/images'),
        ),
    ]
