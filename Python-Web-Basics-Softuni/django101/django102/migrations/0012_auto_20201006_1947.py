# Generated by Django 3.1.1 on 2020-10-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0011_auto_20201006_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='level_of_difficulty',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard'), (4, 'Veteran')], default=1, max_length=2),
        ),
    ]
