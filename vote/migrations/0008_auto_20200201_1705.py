# Generated by Django 2.2.7 on 2020-02-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0007_auto_20200201_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Category',
            field=models.CharField(choices=[('c', 'chairman'), ('s', 'secretary'), ('e', 'Entertainment'), ('t', 'Treasurer'), ('a', 'Academic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Course',
            field=models.CharField(choices=[('m', 'M & I'), ('b', 'BPS'), ('m', 'MMPE'), ('b', 'BCOM'), ('i', 'I & C')], max_length=50),
        ),
    ]
