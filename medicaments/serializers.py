from rest_framework import serializers
from medicaments.models import Medicament

class MedicamentSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Medicament
        fields = ('commercial', 'generique', 'quantite', 'description', 'stock', 'famille', 'image', 'user')
        read_only_fields = ('verified')
