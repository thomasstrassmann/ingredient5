# Generated by Django 3.2.16 on 2022-11-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='email',
            field=models.EmailField(default='Please enter your email here!', max_length=254),
        ),
    ]