# Generated by Django 3.1.7 on 2024-06-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20240618_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/covers'),
        ),
    ]
