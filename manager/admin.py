from django.contrib import admin
from .models import Item, Category


class ItemInLine(admin.TabularInline):
    model = Item
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInLine]


admin.site.register(Item)
admin.site.register(Category, CategoryAdmin)
