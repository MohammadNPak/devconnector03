# Generated by Django 4.0.4 on 2022-06-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='default_profile_picture.jpg', upload_to='profile_picture'),
        ),
    ]
