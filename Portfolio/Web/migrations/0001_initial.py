# Generated by Django 3.0.6 on 2020-07-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_field', models.CharField(choices=[('Front-end', 'Front-end'), ('Back-end', 'Back-end')], max_length=10)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]
