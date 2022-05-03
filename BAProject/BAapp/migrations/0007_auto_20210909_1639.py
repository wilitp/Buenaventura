# Generated by Django 3.1.2 on 2021-09-09 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BAapp', '0006_auto_20210909_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='categoria_iva',
            field=models.CharField(blank=True, choices=[('CF', 'Consumidor Final'), ('MO', 'Monotributo'), ('RI', 'Responsable Inscripto'), ('EX', 'Exento'), ('RIM', 'Responsable Inscripto M')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='itempropuesta',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='BAapp.proveedor'),
        ),
    ]
