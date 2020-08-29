# Generated by Django 3.0.6 on 2020-08-05 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Web', '0007_auto_20200804_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.TextField(max_length=500)),
                ('Link', models.CharField(max_length=100)),
                ('Editor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='technologies',
            old_name='language',
            new_name='Language',
        ),
        migrations.AlterField(
            model_name='skills',
            name='Field',
            field=models.CharField(choices=[('Game-dev', 'Game-dev'), ('Front-end', 'Front-end'), ('Back-end', 'Back-end')], max_length=10),
        ),
        migrations.DeleteModel(
            name='applications',
        ),
    ]