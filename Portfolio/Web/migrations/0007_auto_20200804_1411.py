# Generated by Django 3.0.6 on 2020-08-04 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Web', '0006_auto_20200730_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='Editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='languages',
            name='Editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skills',
            name='Editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='technologies',
            name='Editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Text',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='languages',
            name='Text',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='technologies',
            name='Text',
            field=models.TextField(max_length=20),
        ),
    ]
