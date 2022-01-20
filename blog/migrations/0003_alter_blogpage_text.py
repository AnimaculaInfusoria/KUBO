# Generated by Django 3.2.11 on 2022-01-20 18:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220120_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='text',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock())], default=None),
        ),
    ]
