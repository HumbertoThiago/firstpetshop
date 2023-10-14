# Generated by Django 4.2.6 on 2023-10-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpetshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospedagem',
            name='observacao',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='dt_agendada',
            field=models.DateField(verbose_name='Data Agendada'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='hr_agendada',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Agendada'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='obs',
            field=models.TextField(max_length=255, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='tipo',
            field=models.CharField(choices=[('BANHO', 'BANHO'), ('BANHOTOSA', 'BANHO E TOSA'), ('TOSA', 'TOSA'), ('CLINICO', 'CLINICO')], max_length=30, verbose_name='Tipo de Serviço'),
        ),
    ]
