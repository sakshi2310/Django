# Generated by Django 5.0 on 2023-12-15 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0006_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='user_id',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
