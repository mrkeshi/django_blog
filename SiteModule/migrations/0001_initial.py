# Generated by Django 4.2 on 2023-05-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleSite', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='setting')),
            ],
        ),
    ]