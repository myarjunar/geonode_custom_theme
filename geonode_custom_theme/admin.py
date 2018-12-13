from django.contrib import admin
from .models import AdvancedGeoNodeThemeCustomization

@admin.register(AdvancedGeoNodeThemeCustomization)
class AdvancedGeoNodeThemeCustomizationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Body', {
            'fields': ('body_bg', 'body_color')
        }),
        ('Navigation Bar', {
            'fields': ('logo', 'navbar_bg', 'navbar_color', 'navbar_search_icon_color')
        }),
        ('Jumbotron', {
            'fields': (
                'jumbotron_bg', 'jumbotron_color', 'jumbotron_welcome_title',
                'jumbotron_welcome_content', 'jumbotron_site_description', 'jumbotron_hyperlink_text_color')
        }),
        ('Big Search', {
            'fields': (
                'big_search_bg', 'big_search_title_text_color', 'big_search_search_icon_color',
                'big_search_hyperlink_text_color')
        }),
        ('Datasets', {
            'fields': ('datasets_bg', 'datasets_title_text_color', 'datasets_icon_color', 'datasets_icon_hover_color')
        }),
        ('Showcase', {
            'fields': (
                'showcase_color', 'showcase_icon_color', 'showcase_icon_title_color', 'showcase_icon_hover_color',
                'showcase_title_text_color', 'showcase_sub_text_color', 'showcase_hyperlink_text_color',
                'showcase_button_color', 'showcase_button_text_color')
        }),
        ('Footer', {
            'fields': ('copyright_logo', )
        })
    )
