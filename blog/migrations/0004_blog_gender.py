# Generated by Django 4.0.3 on 2022-03-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_time_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'male'), ('F', 'FEMALE'), ('O', 'OTHERS')], max_length=1),
        ),
    ]