# Generated by Django 5.0.3 on 2024-06-16 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_image_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='additional_images',
        ),
        migrations.RemoveField(
            model_name='route',
            name='type',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]