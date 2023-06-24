# Generated by Django 4.2.2 on 2023-06-23 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookattribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='book.books')),
            ],
        ),
    ]