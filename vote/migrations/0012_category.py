# Generated by Django 2.2.7 on 2020-02-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0011_auto_20200205_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
