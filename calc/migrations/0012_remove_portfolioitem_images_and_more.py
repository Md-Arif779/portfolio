# Generated by Django 4.2.5 on 2023-10-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_remove_portfolioitem_image_portfolioimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='images',
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='portfolio_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='calc.portfolioitem'),
        ),
    ]
