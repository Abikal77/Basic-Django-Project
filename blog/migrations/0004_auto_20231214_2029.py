# Generated by Django 2.0.2 on 2023-12-14 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231214_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_post',
            new_name='blog_des',
        ),
    ]
