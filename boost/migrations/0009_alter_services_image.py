# Generated by Django 3.2.6 on 2022-04-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boost', '0008_alter_services_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(default='', upload_to='boost/images'),
        ),
    ]
