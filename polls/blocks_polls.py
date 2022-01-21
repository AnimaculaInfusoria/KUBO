from .models import Question
from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


class PollsBlock(blocks.StructBlock):
    poll = SnippetChooserBlock(Question)
    class Meta:
        template = 'polls/snippets/poll_snippet.html'
        icon = 'edit'
        label = 'Poll'