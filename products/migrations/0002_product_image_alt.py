# Generated by Django 3.2 on 2023-04-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_alt',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
