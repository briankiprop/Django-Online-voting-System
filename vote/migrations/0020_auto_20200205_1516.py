# Generated by Django 2.2.7 on 2020-02-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0019_auto_20200205_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='Academic',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vote',
            name='Entertainment',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vote',
            name='Treasurer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vote',
            name='chairman',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vote',
            name='secretary',
            field=models.CharField(max_length=50),
        ),
    ]
