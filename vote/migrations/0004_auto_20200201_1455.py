# Generated by Django 2.2.7 on 2020-02-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20200201_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Course',
            field=models.CharField(max_length=50),
        ),
    ]
