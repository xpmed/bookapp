# Generated by Django 5.0.6 on 2024-06-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0016_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
