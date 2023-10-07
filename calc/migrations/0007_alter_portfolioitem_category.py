# Generated by Django 4.2.5 on 2023-10-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_portfolioitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='category',
            field=models.CharField(choices=[('Web', 'Web Development'), ('App', 'App Development'), ('Card', 'Card Design')], default='Web', max_length=10),
        ),
    ]
