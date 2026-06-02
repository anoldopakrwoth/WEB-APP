from django.contrib import admin
from .models import ProduceListing


@admin.register(ProduceListing)
class ProduceListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'quantity', 'village_origin', 'target_town', 'has_video', 'is_available', 'created_at')
    list_filter = ('is_available', 'created_at', 'village_origin', 'target_town')
    search_fields = ('title', 'description', 'seller__username', 'village_origin')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Product Information', {
            'fields': ('title', 'description', 'price', 'quantity', 'image', 'video')
        }),
        ('Location', {
            'fields': ('village_origin', 'target_town')
        }),
        ('Seller & Status', {
            'fields': ('seller', 'is_available', 'created_at')
        }),
    )

    @admin.display(boolean=True, description='Video')
    def has_video(self, obj):
        return bool(obj.video)
