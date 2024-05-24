# Generated by Django 5.0.6 on 2024-05-24 03:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=256, upload_to=uuid.UUID('d64734db-309f-432c-a37a-2e9e6fe893f9'))),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Jpg',
            fields=[
                ('basemedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='media.basemedia')),
            ],
            bases=('media.basemedia',),
        ),
    ]