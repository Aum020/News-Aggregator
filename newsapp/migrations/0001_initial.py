# Generated by Django 3.1.2 on 2020-10-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
                'unique_together': {('title', 'img')},
            },
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
                'unique_together': {('title', 'img')},
            },
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
                'unique_together': {('title', 'img')},
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
                'unique_together': {('title', 'img')},
            },
        ),
    ]
