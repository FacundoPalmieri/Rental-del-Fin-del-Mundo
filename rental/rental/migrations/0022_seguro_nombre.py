# Generated by Django 5.0.3 on 2024-06-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0021_rename_full_seguro_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguro',
            name='nombre',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
