from django import forms
# from bootstrap3_datetime.widgets import DateTimePicker

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        # sender = forms.EmailField()

class signUpForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    nationalID = forms.CharField(max_length=10)
    apartmentID = forms.IntegerField()
    sex = forms.CharField()
    bankAccount = forms.CharField()
    bank = forms.CharField()
    firstName = forms.CharField()
    type = forms.CharField()
    lastName = forms.CharField()
    emailAddress = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(signUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['nationalID'].widget.attrs['class'] = 'form-control'
        self.fields['apartmentID'].widget.attrs['class'] = 'form-control'
        self.fields['sex'].widget.attrs['class'] = 'form-control'
        self.fields['bankAccount'].widget.attrs['class'] = 'form-control'
        self.fields['bank'].widget.attrs['class'] = 'form-control'
        self.fields['firstName'].widget.attrs['class'] = 'form-control'
        self.fields['lastName'].widget.attrs['class'] = 'form-control'
        self.fields['emailAddress'].widget.attrs['class'] = 'form-control'
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


class AddDashbordForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(AddDashbordForm, self).__init__(*args, **kwargs)
        # self.fields['dateAndTime'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'

class AddFacilityForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    availTimes = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(AddFacilityForm, self).__init__(*args, **kwargs)
        # self.fields['dateAndTime'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['availTimes'].widget.attrs['class'] = 'form-control'

class SendMessageForm(forms.Form):
    recievers = forms.CharField()
    title = forms.CharField()
    type = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        # self.fields['dateAndTime'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['recievers'].widget.attrs['class'] = 'form-control'

class EditProfileForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    emailAddress = forms.EmailField()
    apartmentID = forms.IntegerField()
    type = forms.CharField()
    bank = forms.CharField()
    bankAccount = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # self.fields['dateAndTime'].widget.attrs['class'] = 'form-control'
        self.fields['firstName'].widget.attrs['class'] = 'form-control'
        self.fields['lastName'].widget.attrs['class'] = 'form-control'
        self.fields['emailAddress'].widget.attrs['class'] = 'form-control'
        self.fields['apartmentID'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['bank'].widget.attrs['class'] = 'form-control'
        self.fields['bankAccount'].widget.attrs['class'] = 'form-control'


class AddBuilding(forms.Form):
    postalCode = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    number = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        super(AddBuilding, self).__init__(*args, **kwargs)
        # self.fields['dateAndTime'].widget.attrs['class'] = 'form-control'
        self.fields['postalCode'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['street'].widget.attrs['class'] = 'form-control'
        self.fields['number'].widget.attrs['class'] = 'form-control'

class AddApartment(forms.Form):
    buildingPostalCode = forms.CharField()
    floor = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        super(AddApartment, self).__init__(*args, **kwargs)
        self.fields['buildingPostalCode'].widget.attrs['class'] = 'form-control'
        self.fields['floor'].widget.attrs['class'] = 'form-control'

class AddBill(forms.Form):
    title =forms.CharField()
    price = forms.IntegerField()
    due_date = forms.DateField()
    def __init__(self, *args, **kwargs):
        super(AddBill, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['due_date'].widget.attrs['class'] = 'form-control'

class OwnerWarningForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(OwnerWarningForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'

class OwnerContractForm(forms.Form):
    price = forms.IntegerField()
    due_date = forms.DateField()
    def __init__(self, *args, **kwargs):
        super(OwnerContractForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['due_date'].widget.attrs['class'] = 'form-control'
