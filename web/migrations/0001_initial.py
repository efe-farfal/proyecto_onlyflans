# Generated by Django 4.2 on 2024-05-02 23:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('image', models.URLField()),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]
