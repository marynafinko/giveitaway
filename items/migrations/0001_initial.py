# Generated by Django 4.1.3 on 2022-11-20 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100)),
                ('giver', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('Toys', 'Toys'), ('Books', 'Books'), ('Baby and Kids stuff', 'Baby and Kids stuff'), ('Furniture', 'Furniture'), ('Kitchen and Home Appliance', 'Kitchen and Home Appliance'), ('Audio, TV and Photography', 'Audio, TV and Photography'), ('Computers and Software', 'Computers and Software'), ('Mobile Phones', 'Mobile Phones'), ('Bicycles', 'Bicycles'), ('Garden and Patio', 'Garden and Patio'), ('Video Games and Consoles', 'Video Games and Consoles'), ('Car Accessories', 'Car Accessories')], max_length=100)),
                ('condition', models.CharField(choices=[('New', 'New'), ('As Good as New', 'As Good as New'), ('Used', 'Used'), ('Poor', ' Poor')], max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('delivery', models.CharField(choices=[('New', 'New'), ('As Good as New', 'As Good as New'), ('Used', 'Used'), ('Poor', ' Poor')], max_length=30)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+310000000'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]