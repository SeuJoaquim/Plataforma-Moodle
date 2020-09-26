from django import forms

CHOICES = (
        (1, 'Aluno'),
        (2, 'Professor')
    )

class NameForm(forms.Form):
    name = forms.CharField(label='Nome de usuario', max_length=100)
    email = forms.EmailField(label='Email')
    senha = forms.CharField(widget=forms.PasswordInput())
    tipo =forms.MultipleChoiceField(choices=CHOICES)
    # password = forms.(label='Your password')