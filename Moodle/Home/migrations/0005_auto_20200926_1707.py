# Generated by Django 3.1.1 on 2020-09-26 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20200926_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='senha',
        ),
    ]