# Generated by Django 3.2.7 on 2021-09-14 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_image_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='final',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.image'),
        ),
    ]
