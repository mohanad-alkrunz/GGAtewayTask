# Generated by Django 3.2.8 on 2021-10-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]