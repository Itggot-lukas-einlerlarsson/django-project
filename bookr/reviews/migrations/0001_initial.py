# Generated by Django 4.2.9 on 2024-01-11 18:38

from django.db import migrations, models
import django_pg_jsonschema.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django_pg_jsonschema.fields.JSONSchemaField(check_schema_in_db=True, schema={'$schema': 'http://json-schema.org/draft-07/schema#', 'properties': {'email': {'description': 'the publishers email address.', 'type': 'string'}, 'name': {'description': 'the name of the publisher', 'max_length': 50, 'type': 'string'}, 'website': {'minimum': 0, 'type': 'string'}}, 'required': ['name', 'website', 'email'], 'type': 'object'})),
            ],
        ),
    ]
