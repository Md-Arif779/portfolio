# Generated by Django 4.2.5 on 2023-10-07 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_alter_portfolioitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='image',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='client',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='project_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_images/')),
                ('portfolio_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.portfolioitem')),
            ],
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='images',
            field=models.ManyToManyField(related_name='portfolio_items', to='calc.portfolioimage'),
        ),
    ]
