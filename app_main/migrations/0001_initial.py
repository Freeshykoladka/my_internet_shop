# Generated by Django 5.0.1 on 2024-01-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='catalog item')),
                ('slug', models.SlugField(verbose_name='url')),
                ('url', models.CharField(max_length=100)),
                ('is_anchor', models.BooleanField(default=False)),
                ('is_manage', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
