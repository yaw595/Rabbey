# Generated by Django 2.0.7 on 2018-11-23 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181123_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, upload_to='order/%Y/%m/%d'),
        ),
    ]
