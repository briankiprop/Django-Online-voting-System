# Generated by Django 2.2.7 on 2020-02-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_candidate_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Category',
            field=models.CharField(choices=[('m', 'M & I'), ('b', 'BPS'), ('m', 'MMPE'), ('b', 'BCOM'), ('i', 'I & C')], max_length=50),
        ),
    ]
