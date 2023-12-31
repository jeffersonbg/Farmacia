# Generated by Django 4.2.5 on 2023-10-07 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GDRFarmacia', '0005_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoVenda', models.CharField(max_length=100)),
                ('dataCompra', models.DateField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('formaPagamento', models.CharField(max_length=50)),
                ('nomeFuncionario', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GDRFarmacia.cliente')),
                ('listProduto', models.ManyToManyField(to='GDRFarmacia.produto')),
            ],
        ),
    ]
