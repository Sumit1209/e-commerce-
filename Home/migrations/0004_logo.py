# Generated by Django 4.1.3 on 2023-02-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
