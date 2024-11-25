from django import forms
from .models import GuestBook

class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['nama', 'alamat', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control'}),
            'pesan': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),}