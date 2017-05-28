from haystack import indexes
from .models import Medicament, Compagnie

#definition of search indexes

class MedicamentIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    comm  = indexes.CharField(model_attr='commercial')
    gen   = indexes.CharField(model_attr='generique')
    descr = indexes.CharField(model_attr='description')

    def get_model(self):
        return Medicament

class CompagnieIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    nom   = indexes.CharField(model_attr='nom')
    pays  = indexes.CharField(model_attr='pays')

    def get_model(self):
        return Compagnie
