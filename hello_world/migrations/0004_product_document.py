# Generated by Django 5.0.3 on 2024-03-22 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='product_documents/'),
        ),
    ]
