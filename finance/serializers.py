from rest_framework import serializers
from .models import Type, Status, Category, Subcategory, Transaction

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

    def validate(self, data):
        category = data.get('category')
        subcategory = data.get('subcategory')
        type_ = data.get('type')

        # Проверка: подкатегория должна относиться к категории
        if subcategory and subcategory.category != category:
            raise serializers.ValidationError(
                f"Подкатегория '{subcategory}' не принадлежит категории '{category}'."
            )

        # Проверка: категория должна относиться к типу
        if category and category.type != type_:
            raise serializers.ValidationError(
                f"Категория '{category}' не принадлежит типу '{type_}'."
            )

        return data

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
