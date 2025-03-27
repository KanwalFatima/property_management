from django.contrib import admin
from .models import Owner, Property, Feedback

# Customize Owner Admin Panel
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'resident_type')
    search_fields = ('first_name', 'last_name')

# Customize Property Admin Panel
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'zip_code', 'rent_status', 'owner')
    search_fields = ('address', 'city', 'state', 'zip_code')
    list_filter = ('rent_status', 'state')

# Customize Feedback Admin Panel
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('property', 'remarks', 'created_date')
    search_fields = ('property__address', 'remarks')
    list_filter = ('created_date',)

# Register models with their custom admin panels
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Feedback, FeedbackAdmin)
