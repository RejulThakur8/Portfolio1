# Generated by Django 5.1.3 on 2025-01-12 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_contactus_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='shipping_description',
        ),
    ]
