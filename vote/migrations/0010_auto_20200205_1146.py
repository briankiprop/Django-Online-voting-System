# Generated by Django 2.2.7 on 2020-02-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20200201_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Category',
            field=models.TextField(choices=[('c', 'chairman'), ('s', 'secretary'), ('e', 'Entertainment'), ('t', 'Treasurer'), ('a', 'Academic')], max_length=50),
        ),
    ]
