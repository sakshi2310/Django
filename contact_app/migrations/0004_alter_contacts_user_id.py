# Generated by Django 5.0 on 2023-12-15 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0003_contacts_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]
