# Generated by Django 4.1.7 on 2023-03-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_category_options_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['time_joined', 'first_name'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]