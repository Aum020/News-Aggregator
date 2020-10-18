# Generated by Django 3.1.2 on 2020-10-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20201017_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='politics',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='politics',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='politics',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sports',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
