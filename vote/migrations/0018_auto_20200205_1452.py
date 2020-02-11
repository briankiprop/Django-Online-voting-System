# Generated by Django 2.2.7 on 2020-02-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0017_auto_20200205_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Category',
            field=models.CharField(choices=[('Chairman', 'Chairman'), ('Secretary', 'Secretary'), ('Entertainment', 'Entertainment'), ('Treasurer', 'Treasurer'), ('Academic', 'Academic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Gender',
            field=models.TextField(choices=[('m', 'Male'), ('f', 'Female')], default='male', max_length=5),
        ),
    ]
