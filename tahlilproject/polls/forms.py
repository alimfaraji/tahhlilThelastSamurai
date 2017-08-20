from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        # sender = forms.EmailField()

class bankForm(forms.Form):
    card_number = forms.CharField(label='card number', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput)
    cvv2 = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(bankForm, self).__init__(*args, **kwargs)
        self.fields['card_number'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['cvv2'].widget.attrs['class'] = 'form-control'
