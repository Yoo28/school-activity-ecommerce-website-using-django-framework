# Generated by Django 4.2.1 on 2023-05-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0004_rename_customer_name_order_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
