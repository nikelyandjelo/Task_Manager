# Generated by Django 4.1.7 on 2023-03-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='images/default_pfp.jpg', upload_to='images/%Y/%m/%d/'),
        ),
    ]
