# Generated by Django 5.0.6 on 2024-06-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_order_approve_alter_item_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='refundrequest',
            name='state',
            field=models.TextField(null=True),
        ),
    ]
