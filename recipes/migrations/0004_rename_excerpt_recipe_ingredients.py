# Generated by Django 3.2.16 on 2022-12-02 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='excerpt',
            new_name='ingredients',
        ),
    ]
