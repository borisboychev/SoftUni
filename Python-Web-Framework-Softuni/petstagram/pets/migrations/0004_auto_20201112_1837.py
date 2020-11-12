# Generated by Django 3.1.1 on 2020-11-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='', upload_to='pets/'),
            preserve_default=False,
        ),
    ]
