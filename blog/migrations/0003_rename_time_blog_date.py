# Generated by Django 4.0.3 on 2022-03-27 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_description_alter_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='time',
            new_name='date',
        ),
    ]
