# Generated by Django 5.1.2 on 2024-11-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_mensagem_lida'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='cidade',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
