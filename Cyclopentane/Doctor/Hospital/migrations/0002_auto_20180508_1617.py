# Generated by Django 2.0.5 on 2018-05-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]