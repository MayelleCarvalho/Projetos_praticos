# Generated by Django 2.0 on 2018-12-28 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questao',
            old_name='data_publcacao',
            new_name='data_publicacao',
        ),
    ]
