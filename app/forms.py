# knapsack_app/forms.py
from django import forms
from .models import Item

class KnapsackForm(forms.Form):
    capacity = forms.IntegerField(label='Kapasitas Kantong')
    num_items = forms.IntegerField(label='Jumlah Barang')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            num_items = int(self.data['num_items'])
        except (KeyError, ValueError):
            num_items = 0

        for i in range(num_items):
            self.fields[f'name_{i}'] = forms.CharField(label=f'Barang-{i + 1} Nama')
            self.fields[f'price_{i}'] = forms.IntegerField(label=f'Barang-{i + 1} Harga')
            self.fields[f'weight_{i}'] = forms.IntegerField(label=f'Barang-{i + 1} Berat')
