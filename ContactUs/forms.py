from django import forms


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class') or ''
                    classes += " border-error"
                    self.fields[f_name].widget.attrs['class'] = classes

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your name...",
        'class':''

    }), error_messages={'required': 'name field is required.'})
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Message",
        'rows': 6
    }), error_messages={'required': 'message field is required.'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': "Email...",
    }), error_messages={'required': 'Email field is required.'})
    website = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': "Website...",
    }), required=False)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
