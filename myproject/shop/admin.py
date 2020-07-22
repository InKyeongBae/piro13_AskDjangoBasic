from django.contrib import admin
from .models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['pk','name','short_desc','price']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['updated_at']

    def short_desc(self,item):
        return item.desc[:20]
    pass