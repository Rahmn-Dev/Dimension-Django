# Generated by Django 5.0 on 2023-12-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_container_capacity_container_capacity_length_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity_weight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
