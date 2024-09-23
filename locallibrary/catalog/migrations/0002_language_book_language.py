# Generated by Django 5.1.1 on 2024-09-22 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('es', 'Spanish'), ('de', 'German'), ('fr', 'French'), ('sa', 'Sanskrit')], default='en', help_text='Language of the book', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.language'),
        ),
    ]
