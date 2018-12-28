from haystack import indexes
from .models import Doubans,Biancheng,Keji

class DoubansIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)


    def get_model(self):
        return Doubans

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class BianchengIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)


    def get_model(self):
        return Biancheng

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class KejiIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)


    def get_model(self):
        return Keji

    def index_queryset(self, using=None):
        return self.get_model().objects.all()