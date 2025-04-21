from django import forms
from .models import Transaction

class TransactionAdminForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        type_ = cleaned_data.get('type')

        if subcategory and subcategory.category != category:
            raise forms.ValidationError(
                f"Подкатегория '{subcategory}' не принадлежит категории '{category}'."
            )

        if category and category.type != type_:
            raise forms.ValidationError(
                f"Категория '{category}' не принадлежит типу '{type_}'."
            )

        return cleaned_data
