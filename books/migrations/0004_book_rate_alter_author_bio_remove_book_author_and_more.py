# Generated by Django 4.0.4 on 2022-04-13 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_kind_alter_book_options_book_genres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.FloatField(default=0, help_text='Enter between 1 - 100', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='plot',
            field=models.TextField(blank=True),
        ),
    ]
