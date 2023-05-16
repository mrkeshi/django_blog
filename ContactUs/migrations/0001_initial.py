# Generated by Django 4.2 on 2023-04-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=50, verbose_name='email address')),
                ('website', models.URLField(blank=True, null=True, verbose_name='website url')),
                ('message', models.TextField(verbose_name='text message')),
            ],
        ),
    ]