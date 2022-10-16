from django import forms
from .models import User, Job
from tinymce.widgets import TinyMCE

class CreateAdForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows': 30}))

    class Meta:
        model = Job
        fields = "__all__"

