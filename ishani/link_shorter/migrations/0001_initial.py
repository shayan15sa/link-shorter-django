# Generated by Django 4.0.6 on 2022-08-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainUrl', models.CharField(max_length=3500)),
                ('shortUrl', models.CharField(max_length=20)),
            ],
        ),
    ]
