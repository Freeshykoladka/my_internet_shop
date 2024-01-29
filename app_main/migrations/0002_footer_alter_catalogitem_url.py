# Generated by Django 5.0.1 on 2024-01-18 16:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', ckeditor.fields.RichTextField()),
                ('reservation', ckeditor.fields.RichTextField()),
                ('opening_hours', ckeditor.fields.RichTextField()),
                ('twitter_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('copyright_text', ckeditor.fields.RichTextField()),
                ('credits_text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]