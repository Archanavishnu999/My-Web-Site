# Generated by Django 4.2.6 on 2023-11-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
