# Generated by Django 4.1.3 on 2022-12-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
