from django import forms
from .models import Profile, Message


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['size'] = 60

    class Meta:
        model = Profile
        fields = (
            'external_id',
            'name'
            )
        widgets = {
            'name': forms.TextInput,
            }


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['size'] = 35
        self.fields['region'].widget.attrs['size'] = 35
        self.fields['dealer_company'].widget.attrs['size'] = 35
        self.fields['type_car'].widget.attrs['size'] = 35
        self.fields['model'].widget.attrs['size'] = 35
        self.fields['dealership'].widget.attrs['size'] = 35

    class Meta:
        model = Message
        fields = (
            'profile',
            'cat',
            'text',
            'region',
            'dealer_company',
            'type_car',
            'model',
            'dealership'
            )
        widgets = {
            'text': forms.TextInput,
            'region': forms.TextInput,
            'dealer_company': forms.TextInput,
            'type_car': forms.TextInput,
            'model': forms.TextInput,
            'dealership': forms.TextInput,
            }
