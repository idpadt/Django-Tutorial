# Generated by Django 4.2.1 on 2023-05-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionrecord',
            name='type',
            field=models.CharField(choices=[('Pengeluaran', 'Pengeluaran'), ('Pemasukan', 'Pemasukan')], max_length=20),
        ),
    ]