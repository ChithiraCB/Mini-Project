# Generated by Django 4.2.5 on 2023-11-02 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_alter_product_quantity_alter_product_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='stock',
        ),
    ]
