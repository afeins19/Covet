from sre_constants import IN
from django import forms 

from .models import Item

'''Save styling for input fields as a variable for reuse'''
INPUT_CLASSES = 'w-full py-4 px-6 bg-gray-100 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta: #override default ModelForm class with custom fields 
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })            
        }

class EditItemForm(forms.ModelForm):
    class Meta:     #override default ModelForm class
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })            
        }