# Generated by Django 5.0.3 on 2024-04-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_alter_auto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
