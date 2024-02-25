from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import PublishingPanel, FieldPanel
from .models import Chapter, Unit, Topic, Problem

class ChapterViewSet(SnippetViewSet):
    model = Chapter
    search_fields = ['chapter_name']
    list_display = ['chapter_number', 'chapter_name']
    list_export = ['chapter_number', 'chapter_name', 'noof_units']
    list_filter = {
        'chapter_number': ['gte'],
        'noof_units': ['lte']
    }
    panels = [ 
        FieldPanel('chapter_number'),
        FieldPanel('chapter_name'),
        FieldPanel('chapter_description'),
        FieldPanel('noof_units'),
        FieldPanel('chapter_video'),
        PublishingPanel() 
    ]
    
class UnitViewSet(SnippetViewSet):
    model = Unit
    search_fields = ['unit_name']
    list_display = ['unit_number', 'unit_name']
    list_export = ['unit_number', 'unit_name', 'noof_units']
    list_filter = {
        'unit_number': ['gte'],
        'noof_units': ['lte']
    }
    panels = [ 
        FieldPanel('unit_number'),
        FieldPanel('unit_name'),
        FieldPanel('unit_description'),
        FieldPanel('noof_units'),
        FieldPanel('unit_video'),
        PublishingPanel() 
    ]
    
register_snippet(ChapterViewSet)