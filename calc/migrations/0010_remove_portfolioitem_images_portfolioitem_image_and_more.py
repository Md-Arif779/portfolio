# Generated by Django 4.2.5 on 2023-10-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_remove_portfolioitem_image_portfolioitem_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='images',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='image',
            field=models.ImageField(default=1, upload_to='portfolio_images/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PortfolioImage',
        ),
    ]
