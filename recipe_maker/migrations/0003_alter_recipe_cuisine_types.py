# Generated by Django 3.2.18 on 2023-04-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_maker', '0002_auto_20230405_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine_types',
            field=models.CharField(choices=[('african', 'African'), ('american', 'American'), ('asian', 'Asian'), ('middle_eastern', 'Middle Eastern'), ('brazilian', 'Brazilian'), ('indian', 'Indian'), ('european', 'European')], default='african', max_length=50),
        ),
    ]
