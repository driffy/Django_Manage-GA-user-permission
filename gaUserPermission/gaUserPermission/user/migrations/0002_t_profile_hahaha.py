# Generated by Django 2.0.2 on 2018-02-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_profile',
            name='hahaha',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
