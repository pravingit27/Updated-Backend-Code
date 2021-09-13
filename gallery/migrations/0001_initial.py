# Generated by Django 3.2.7 on 2021-09-07 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='gallery.category')),
                ('size_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size_name', to='gallery.size')),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('image_name', models.CharField(max_length=300)),
                ('amount', models.FloatField(blank=True, default=True, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='gallery.meet')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]