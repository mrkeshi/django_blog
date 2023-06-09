# Generated by Django 4.2 on 2023-05-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_productcategories_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategories',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='url categories'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='slug'),
        ),
    ]
