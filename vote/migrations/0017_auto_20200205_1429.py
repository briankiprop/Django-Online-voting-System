# Generated by Django 2.2.7 on 2020-02-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0016_auto_20200205_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='YearSem',
            field=models.CharField(choices=[('Y1S1', 'Y1S1'), ('Y1S2', 'Y1S2'), ('Y2S1', 'Y2S1'), ('Y2S2', 'Y2S2'), ('Y3S1', 'Y3S1'), ('Y3S2', 'Y3S2'), ('Y4S1', 'Y4S1'), ('Y4S2', 'Y4S2')], max_length=4),
        ),
    ]