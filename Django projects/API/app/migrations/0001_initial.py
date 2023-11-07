# Generated by Django 3.2.23 on 2023-11-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(default='Description')),
            ],
        ),
    ]
