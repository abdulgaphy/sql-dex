from django import forms
from . validation import validate_dot_com, validate_url

class urlForm(forms.Form):
    url = forms.URLField(label='',
                    validators=[validate_url, validate_dot_com],
                    widget =forms.TextInput(
                    attrs ={
                    "class":"form-control mr-sm-2 ",
                    "placeholder":"Enter URL",
                    "autocomplete": "off",
                }
                )
            )
        
class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder":"Your full name"
                        }
                    )
                )
    email = forms.EmailField(
                widget=forms.EmailInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Enter your Email"
                    }
                ))

    comment = forms.CharField(
            widget=forms.Textarea(
                attrs={
                        "class":"form-control",
                        "placeholder": "Come on! talk to us."
                        }
                                  )
                            )

    