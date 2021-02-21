# Generated by Django 3.1.6 on 2021-02-19 18:58

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_storage', '0003_auto_20210218_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mp3', models.FileField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='audios/', validators=[cloudinary_storage.validators.validate_video])),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='mp4',
            field=models.FileField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='videos/', validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]
