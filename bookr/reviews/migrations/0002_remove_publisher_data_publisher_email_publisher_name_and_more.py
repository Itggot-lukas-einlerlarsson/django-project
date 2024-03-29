# Generated by Django 4.2.9 on 2024-01-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='data',
        ),
        migrations.AddField(
            model_name='publisher',
            name='email',
            field=models.EmailField(default=None, help_text="the publisher's email address.", max_length=254),
        ),
        migrations.AddField(
            model_name='publisher',
            name='name',
            field=models.CharField(default=None, help_text='the name of the publisher.', max_length=50),
        ),
        migrations.AddField(
            model_name='publisher',
            name='website',
            field=models.URLField(default=None, help_text="the publisher's website."),
        ),
    ]
