from django import forms
from .models import List, CarList


class ListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget.attrs['size'] = 30

    class Meta:
        model = List
        fields = (
            'region',
            'name'
            )
        widgets = {
            'region': forms.TextInput,
        }


class CarListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarListForm, self).__init__(*args, **kwargs)
        self.fields['type_car2'].widget.attrs['size'] = 50
        self.fields['quantity'].widget.attrs['size'] = 6
        self.fields['name'].widget.attrs['size'] = 40

    class Meta:
        model = CarList
        fields = (
            'type_car',
            'type_car2',
            'quantity',
            'name',
            'car_info'
            )

        widgets = {
            'type_car2': forms.TextInput,
            'quantity': forms.TextInput,
            'name': forms.TextInput,
            }
