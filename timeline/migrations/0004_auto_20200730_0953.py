# Generated by Django 3.0.6 on 2020-07-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_remove_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_pic.png', upload_to='timeline_pics'),
        ),
    ]
