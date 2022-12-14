# Generated by Django 4.1 on 2022-10-09 19:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=50, verbose_name='Nome da Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=20, verbose_name='Nome do Produto/Serviço')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do Produto/Serviço')),
                ('product_photo', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Foto do Produto')),
                ('product_description', models.TextField(blank=True, null=True, verbose_name='Descrição do produto')),
                ('product_bar_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Codigo de Barras')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
