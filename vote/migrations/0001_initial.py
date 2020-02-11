# Generated by Django 2.2.7 on 2020-02-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.TextField()),
                ('LastName', models.TextField()),
                ('Reg_No', models.CharField(max_length=20)),
                ('YearSem', models.CharField(max_length=4)),
                ('profilePic', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
    ]
