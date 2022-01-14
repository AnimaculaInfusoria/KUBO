# Generated by Django 3.2.11 on 2022-01-14 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0002_delete_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_title', models.CharField(blank=True, help_text='Main text displayed in the hero section over the background.', max_length=120)),
                ('hero_subtitle', models.TextField(blank=True, help_text='Subtitle following the main title in the hero section.', max_length=200)),
                ('cta_btn_text', models.CharField(blank=True, default='Learn More', help_text='Call-To-Action Button Text', max_length=20)),
                ('background_image', models.ForeignKey(help_text='Header background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('cta_btn_link', models.ForeignKey(blank=True, help_text='Internal page link to send the user to when clicking CTA button.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
