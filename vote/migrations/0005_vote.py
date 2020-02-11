# Generated by Django 2.2.7 on 2020-02-01 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0004_auto_20200201_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chairman', models.CharField(max_length=50)),
                ('secretary', models.CharField(max_length=50)),
                ('Entertainment', models.CharField(max_length=50)),
                ('Treasurer', models.CharField(max_length=50)),
                ('Academic', models.CharField(max_length=50)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]