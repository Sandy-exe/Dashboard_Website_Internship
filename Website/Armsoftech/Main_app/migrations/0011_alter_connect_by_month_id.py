# Generated by Django 4.2.6 on 2023-10-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0010_alter_connect_by_month_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect_by_month',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]