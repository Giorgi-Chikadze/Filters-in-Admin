from django.contrib import admin
from shop.models import Tag, Item, Category
from shop.filters import PriceFilter

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1


class TagItemInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1
    

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    autocomplete_fields = ['items']
    inlines = [TagItemInline]
    
    

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']
    search_fields = ['name']
    ordering = ['price']
    autocomplete_fields = ['category']
    fields = ['name', 'category', 'price', 'description']
    inlines = [TagItemInline]
    list_filter = [PriceFilter]
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','get_five_items']
    search_fields = ['name', 'id', 'item__name']
    ordering = ['name', 'id']
    list_per_page = 100
    inlines = [ItemInline]    
    
    def get_five_items(self, category):
        items = category.items.all()[:5]
        empty_list = []
        for item in items:
            empty_list.append(item.name) 
        return empty_list if empty_list else "no items found"
    
    
    def get_queryset(self, request):
        existing_queryset = super().get_queryset(request)
        return existing_queryset.prefetch_related('items')

admin.site.register(Tag, TagAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)


