# Generated by Django 5.0 on 2023-12-15 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='user_id',
            field=models.IntegerField(default=''),
        ),
    ]
