from django import forms
from django.core import validators

'''def starts_with_s(value):
    print('starts_with_s function execution')
    if value[0].lower() != 's':
        raise forms.ValidationError('Name should be starts with s or S')
    
def clean_rollno(self):
        print('Validating rollno field')
        inputrollno = self.cleaned_data['rollno']
        return inputrollno

def gmail_validator(value):
    print('checking for  gemail Validating')
    if value[-10:]!='@gmail.com':
        raise forms.ValidationError('Mail extension should be gmail')

def clean_feedback(self):
    print('Validating feedback field')
    inputfeedback=self.cleaned_data['feedback']
    return inputfeedback

class FeedBackForm(forms.Form):
    name=forms.CharField(validators=[starts_with_s])
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_validator])
    feedback =forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)'''

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(label='Enter Password',widget=forms.PasswordInput)
    Rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback =forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

    def clean(self):
        print('Total form validation.....')
        total_cleaned_data = super().clean()
        print('Validating Name')
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 'm':
            raise forms.ValidationError('name should be starts with m')
        inputrollno = total_cleaned_data['rollno']
        print('Validating rollno')
        if inputrollno <= 0:
            raise forms.ValidationError('Rollno should be >0')
        inputemail = total_cleaned_data['email']
        print('Validating email')
        if inputemail[-10:] !='@gmail.com':
            raise forms.ValidationError('Email extension should be gmail')
        print('validating password')
        total_cleaned_data=super().clean()
        password = total_cleaned_data['password']
        Rpassword = total_cleaned_data['Rpassword']
        if password != Rpassword:
            raise forms.ValidationError('Both passwords must be same.......')