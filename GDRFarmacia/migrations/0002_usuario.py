# Generated by Django 4.2.3 on 2023-09-27 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GDRFarmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GDRFarmacia.endereco')),
            ],
        ),
    ]