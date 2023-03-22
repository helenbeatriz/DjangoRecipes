# Generated by Django 3.2.18 on 2023-03-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('image', models.ImageField(upload_to='recipes')),
            ],
        ),
    ]