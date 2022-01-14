from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel 
from wagtail.images.edit_handlers import ImageChooserPanel 


class HomePage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )
    
    hero_title = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section over the background."
    )

    hero_subtitle = models.TextField(
        max_length=200,
        blank=True,
        help_text="Subtitle following the main title in the hero section."
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("cta_btn_text"),
        PageChooserPanel("cta_btn_link"),
        ImageChooserPanel("background_image"), 
        
    ]

    cta_btn_text = models.CharField(
        max_length=20,
        blank=True,
        default="Learn More",
        help_text="Call-To-Action Button Text",
    )

    cta_btn_link = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Internal page link to send the user to when clicking CTA button."
    )

    