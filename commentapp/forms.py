from django.forms import ModelForm
from .models import comm

class CommentForm(ModelForm):
    class Meta:
        model = comm
        fields = '__all__'
