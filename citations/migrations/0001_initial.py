# Generated by Django 3.2.12 on 2022-06-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('citation_code', models.CharField(max_length=33, primary_key=True, serialize=False, verbose_name='Citation code')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('volume', models.CharField(blank=True, max_length=127, null=True, verbose_name='Volume')),
                ('year', models.SmallIntegerField(verbose_name='Year')),
            ],
        ),
    ]
