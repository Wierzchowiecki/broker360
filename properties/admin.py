from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

    fields = (
        "image",
        "description",
        "is_main",
    )


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "property_type",
        "offer_type",
        "city",
        "price",
        "status",
        "is_featured",
    )

    list_filter = (
        "property_type",
        "offer_type",
        "status",
        "is_featured",
    )

    search_fields = (
        "title",
        "city",
        "district",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        PropertyImageInline,
    ]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = (
        "property",
        "description",
        "is_main",
        "created_at",
    )

    list_filter = (
        "is_main",
        "created_at",
    )

    search_fields = (
        "property__title",
        "description",
    )

    readonly_fields = (
        "created_at",
    )