from haystack import indexes
from .models import Medicament

#definition of search indexes

class MedicamentIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    comm  = indexes.CharField(model_attr='commercial')
    gen   = indexes.CharField(model_attr='generique')
    descr = indexes.CharField(model_attr='description')

    def get_model(self):
        return Medicament
