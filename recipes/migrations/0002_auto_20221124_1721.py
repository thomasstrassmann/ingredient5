# Generated by Django 3.2.16 on 2022-11-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.IntegerField(blank=True, choices=[(0, 'Unassignable'), (1, 'European'), (2, 'Asian'), (3, 'Arabic'), (4, 'African'), (5, 'North-/Southamerican')], null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(),
        ),
    ]
