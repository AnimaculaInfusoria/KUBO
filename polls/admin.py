from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Question, Choice

class Choiceline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [Choiceline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


class PollsAdmin(ModelAdmin):
    model = Question
    menu_label = "Polls"
    menu_icon = "plus"
    inlines = [Choiceline]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']

modeladmin_register(PollsAdmin)

