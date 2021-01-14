import re
from django import forms
def password_validator(value):
    if (len(value) < 6 ):
        raise forms.ValidationError('password length should be 6')
    elif not re.search("[a-z]", value):
        raise forms.ValidationError('password should contain atleast one lowercase letter')
    elif not re.search("[0-9]", value):
        raise forms.ValidationError('password should contain atleast one digit letter')
    elif not re.search("[A-Z]", value):
        raise forms.ValidationError('password should contain atleast one Upper Case letter')
    elif not re.search("[_$#@!%&^*]", value):
        raise forms.ValidationError('password should contain atleast one Special Character')

def contact_no_validator(value):
    regex=r'^\+?1?\d{9,15}$'
    if not re.match(regex,str(value)):
        raise forms.ValidationError("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    user_name = forms.CharField(required=True)
    email_id = forms.EmailField(required=True)
    country = forms.CharField(max_length="50",required=True)
    birth_date = forms.DateField(help_text ="dd/mm/yyyy ")
    contact_no = forms.IntegerField(required=True,validators=[contact_no_validator])
    password = forms.CharField(widget=forms.PasswordInput,validators=[password_validator])
    rpassword = forms.CharField(widget=forms.PasswordInput,required=True,label="Re Enter Password")

    def clean(self):
        super(UserRegistrationForm, self).clean()
        # This method will set the `cleaned_data` attribute

        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('rpassword')
        if not password == re_password:
            raise forms.ValidationError('Passwords must match')

class UserLogInForm(forms.Form):
    user_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)