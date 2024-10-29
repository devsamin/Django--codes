# Generated by Django 5.1.1 on 2024-10-09 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
            ],
        ),
    ]
