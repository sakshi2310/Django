# Generated by Django 5.0 on 2023-12-15 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0004_alter_contacts_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contacts',
        ),
    ]
