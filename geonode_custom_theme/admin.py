from django.contrib import admin

from geonode_custom_theme.admin_actions import enable_theme, disable_theme
from .models import AdvancedGeoNodeThemeCustomization

@admin.register(AdvancedGeoNodeThemeCustomization)
class AdvancedGeoNodeThemeCustomizationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None ,{
            'fields': ('name', )
        }),
        ('Body', {
            'fields': ('body_bg', 'body_color')
        }),
        ('Navigation Bar', {
            'fields': ('logo', 'navbar_bg', 'navbar_color', 'navbar_hover_color', 'navbar_search_icon_color')
        }),
        ('Jumbotron', {
            'fields': (
                'jumbotron_bg', 'jumbotron_color', 'jumbotron_welcome_title',
                'jumbotron_welcome_content', 'jumbotron_site_description', 'jumbotron_hyperlink_text_color',
                'jumbotron_button_hide', 'jumbotron_button_text', 'jumbotron_button_link', 'jumbotron_button_color')
        }),
        ('Big Search', {
            'fields': (
                'big_search_bg', 'big_search_color', 'big_search_title', 'big_search_placeholder',
                'big_search_hyperlink_text', 'big_search_title_text_color', 'big_search_search_icon_color',
                'big_search_hyperlink_text_color')
        }),
        ('Datasets', {
            'fields': ('datasets_bg', 'datasets_title', 'datasets_title_text_color',
                       'datasets_icon_color', 'datasets_icon_hover_color')
        }),
        ('Showcase', {
            'fields': (
                'showcase_color', 'showcase_title', 'showcase_icon_color', 'showcase_icon_title_color',
                'showcase_icon_hover_color', 'showcase_title_text_color', 'showcase_sub_text_color',
                'showcase_hyperlink_text_color', 'showcase_button_color', 'showcase_button_text_color')
        }),
        ('Footer', {
            'fields': ('footer_bg', 'copyright_logo')
        }),
        ('Components', {
            'fields': ('primary_button_color', 'primary_button_hover_color')
        })
    )

    list_display = ('id', 'is_enabled', 'name', 'date', 'description')
    list_display_links = ('id', 'name',)
    actions = [enable_theme, disable_theme]
