# Generated by Django 5.0 on 2024-01-02 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_data', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categorias de Productos',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_data', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcionm')),
            ],
            options={
                'verbose_name': 'Unidad de medida',
                'verbose_name_plural': 'Unidades de medidas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_data', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre del Producto')),
                ('description', models.TextField(verbose_name='Descripcion del Producto')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Idicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_data', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('descount_value', models.PositiveSmallIntegerField()),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproducts', verbose_name=' Indicador de Oferta')),
            ],
            options={
                'verbose_name': 'Indicador de ofertas1',
                'verbose_name_plural': 'Indicadorres de ofertass',
            },
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
    ]