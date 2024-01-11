# Generated by Django 4.2.9 on 2024-01-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_publisher_data_publisher_email_publisher_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(default=None, help_text="The contributor's first name or names.", max_length=50)),
                ('last_names', models.CharField(default=None, help_text="The contributor's lastname or names.", max_length=50)),
                ('email', models.EmailField(default=None, help_text='The contact email for the contributor.', max_length=254)),
            ],
        ),
    ]