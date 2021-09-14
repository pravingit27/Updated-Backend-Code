# Generated by Django 3.2.7 on 2021-09-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='item_url',
            field=models.URLField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
    ]