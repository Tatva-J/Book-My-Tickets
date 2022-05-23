# Generated by Django 4.0.4 on 2022-05-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(default=' ', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
