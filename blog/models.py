from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel 
from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from polls.models import Question
from polls import blocks_polls


class BlogListingPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    headline_text = models.CharField(
        max_length=70,
        blank=True, 
        help_text='Blog listing page header text.'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"), 
        FieldPanel("headline_text")
        ]

class BlogPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    poll = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='+')
    text = StreamField([
        ('text_fill', blocks.RichTextBlock()),
        ('polls', blocks_polls.PollsBlock()),
    ], default=None)

    # Editor panels configuration

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        StreamFieldPanel('text'),
        FieldPanel('owner'),
    ]