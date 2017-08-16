from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=30)
    password = password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        # sender = forms.EmailField()