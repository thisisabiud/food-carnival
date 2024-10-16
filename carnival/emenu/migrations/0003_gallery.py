# Generated by Django 5.1.1 on 2024-10-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emenu', '0002_menu_category_alter_menu_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('description', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
