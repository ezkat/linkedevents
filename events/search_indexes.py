from haystack import indexes
from .models import Event, Place, PublicationStatus
from django.utils.translation import get_language
from django.utils.html import strip_tags

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    autosuggest = indexes.EdgeNgramField(model_attr='name')
    end_time = indexes.DateField(model_attr='end_time')

    def get_updated_field(self):
        return 'last_modified_time'

    def get_model(self):
        return Event

    def prepare(self, obj):
        #obj.lang_keywords = obj.keywords.filter(language=get_language())
        if obj.description:
            obj.description = strip_tags(obj.description)
        return super(EventIndex, self).prepare(obj)

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(publication_status=PublicationStatus.PUBLIC)


class PlaceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    autosuggest = indexes.EdgeNgramField(model_attr='name')

    def get_updated_field(self):
        return 'last_modified_time'

    def get_model(self):
        return Place
