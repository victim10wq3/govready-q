# Generated by Django 3.0.7 on 2020-09-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0028_poam_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poam',
            name='poam_group',
            field=models.CharField(blank=True, help_text='A name to collect related POA&Ms together.', max_length=50, null=True),
        ),
    ]
