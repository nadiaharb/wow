# Generated by Django 3.2.6 on 2022-04-27 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boost', '0010_alter_services_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
    ]