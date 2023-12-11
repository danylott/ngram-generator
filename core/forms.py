from django import forms

class NgramForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Введіть текст')
    n = forms.IntegerField(min_value=2, max_value=7, label='Введіть n для n-грам')
