# Generated by Django 2.2.7 on 2020-02-01 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Candidates',
            new_name='Candidate',
        ),
    ]
