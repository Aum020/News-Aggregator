# Generated by Django 3.1.2 on 2020-10-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='img',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='politics',
            name='img',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='politics',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='img',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='entertainment',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='politics',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='sports',
            unique_together=set(),
        ),
    ]
