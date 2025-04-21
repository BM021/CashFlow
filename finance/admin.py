from django.contrib import admin
from .models import Type, Status, Category, Subcategory, Transaction
from .forms import TransactionAdminForm
# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm
    list_display = ('created_at', 'type', 'status', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('type', 'status', 'category', 'subcategory')
    search_fields = ('comment',)


admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Subcategory)
