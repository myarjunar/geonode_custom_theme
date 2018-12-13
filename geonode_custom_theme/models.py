from django.db import models
from geonode.client.models import GeoNodeThemeCustomization

# Extend GeoNodeThemeCustomization model

class AdvancedGeoNodeThemeCustomization(GeoNodeThemeCustomization):
    """Extend non-covered customization from GeoNodeThemeCustomization"""

    # Body section
    # below field will affect the background image of the footer
    body_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Datasets background")

    # Navbar section
    navbar_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Navbar background")
    navbar_search_icon_color = models.CharField(max_length=10, default="#333333")

    # Jumbotron section
    jumbotron_hyperlink_text_color = models.CharField(max_length=10, default="#333333")

    # Big search section
    big_search_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Big search background")
    big_search_title_text_color = models.CharField(max_length=10, default="#333333")
    big_search_hyperlink_text_color = models.CharField(max_length=10, default="#333333")
    big_search_search_icon_color = models.CharField(max_length=10, default="#333333")

    # Datasets section
    datasets_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Datasets background")
    datasets_title_text_color = models.CharField(max_length=10, default="#333333")
    datasets_icon_color = models.CharField(max_length=10, default="#333333")
    datasets_icon_hover_color = models.CharField(max_length=10, default="#333333")

    # Showcase section
    showcase_color = models.CharField(max_length=10, default="#333333")
    showcase_title_text_color = models.CharField(max_length=10, default="#333333")
    showcase_sub_text_color = models.CharField(max_length=10, default="#333333")
    showcase_icon_color = models.CharField(max_length=10, default="#333333")
    showcase_icon_title_color = models.CharField(max_length=10, default="#333333")
    showcase_icon_hover_color = models.CharField(max_length=10, default="#333333")
    showcase_button_color = models.CharField(max_length=10, default="#333333")
    showcase_button_text_color = models.CharField(max_length=10, default="#333333")
    showcase_hyperlink_text_color = models.CharField(max_length=10, default="#333333")

    # Footer section
    copyright_logo = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Datasets background")

    class Meta:
        ordering = ("date",)
        verbose_name_plural = 'Advanced Themes'
