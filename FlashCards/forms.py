from django.forms import ModelForm
from .models import Cards
class CardForm(ModelForm):
    class Meta:
        model = Cards
        fields = ['subject', 'question', 'answer']