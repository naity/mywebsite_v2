# Generated by Django 2.1.3 on 2018-11-14 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('authors', models.TextField()),
                ('abstract', models.TextField()),
                ('figure', models.ImageField(upload_to='research/publications/figures')),
                ('pdf', models.FileField(upload_to='research/publications/pdfs')),
                ('pub_date', models.DateField()),
                ('downloads', models.PositiveIntegerField(default=0)),
                ('last_downloaded', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
