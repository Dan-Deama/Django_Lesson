# Generated by Django 5.0.3 on 2024-03-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField(null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]