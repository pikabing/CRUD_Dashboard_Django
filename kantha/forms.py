from django import forms

class AdminForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password:'}),max_length=20)