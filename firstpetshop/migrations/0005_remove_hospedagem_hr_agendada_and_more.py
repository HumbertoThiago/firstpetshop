# Generated by Django 4.2.6 on 2023-10-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpetshop', '0004_pet_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospedagem',
            name='hr_agendada',
        ),
        migrations.AlterField(
            model_name='hospedagem',
            name='dt_agendada',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Agendada'),
        ),
    ]
