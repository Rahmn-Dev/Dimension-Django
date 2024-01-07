from django import forms
from .models import Item, Container, Truck

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'weight', 'price', 'length', 'width', 'value']

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name', 'capacity_weight', 'capacity_length', 'capacity_width']
        
class KnapsackForm(forms.Form):
    capacity = forms.IntegerField(label='Kapasitas Kantong', required=False)  # Buat capacity tidak wajib
    container = forms.ModelChoiceField(queryset=Container.objects.all())
    items = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields['capacity'].widget = forms.HiddenInput()

       
        self.fields['items'].choices = [(item.id, item.name) for item in Item.objects.all()]

    def clean_items(self):
        items = self.cleaned_data['items']
        if not items:
            raise forms.ValidationError('Anda harus memilih setidaknya satu item.')

        return items

    

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['name', 'capacity_weight',]