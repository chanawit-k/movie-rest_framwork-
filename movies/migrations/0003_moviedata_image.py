# Generated by Django 3.1 on 2022-04-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/None/Noimg.jpg', upload_to='images/'),
        ),
    ]
