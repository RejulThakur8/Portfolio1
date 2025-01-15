from django import forms
from .models import Contactus

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=['Name','Email','Phone','Subject','Message']
        widgets={
            'Name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter Your Name'}),
            'Email': forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter Your Mail"}),
            'Phone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
            'Subject' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter Your Subject'}),
            'Message' : forms.Textarea(attrs={'class' : 'form-control','placeholder':'Enter Your Messages'}),
        }