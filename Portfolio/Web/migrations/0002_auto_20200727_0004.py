# Generated by Django 3.0.6 on 2020-07-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web_skills',
            name='dev_field',
        ),
        migrations.RemoveField(
            model_name='web_skills',
            name='text',
        ),
        migrations.AddField(
            model_name='web_skills',
            name='Field',
            field=models.CharField(blank=True, choices=[('Front-end', 'Front-end'), ('Back-end', 'Back-end')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='web_skills',
            name='Text',
            field=models.TextField(blank=True, default=None, max_length=1000),
        ),
    ]
