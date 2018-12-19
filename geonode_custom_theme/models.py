from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from geonode.client.models import GeoNodeThemeCustomization

# Extend GeoNodeThemeCustomization model

class AdvancedGeoNodeThemeCustomization(GeoNodeThemeCustomization):
    """Extend non-covered customization from GeoNodeThemeCustomization"""

    """Home page"""

    # Body section
    # below field will affect the background image of the footer
    body_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Datasets background")

    # Navbar section
    navbar_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Navbar background")
    navbar_search_icon_color = models.CharField(max_length=50, null=True, blank=True)

    # Jumbotron section
    jumbotron_hyperlink_text_color = models.CharField(max_length=50, null=True, blank=True)

    # Big search section
    big_search_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Big search background")
    big_search_color = models.CharField(max_length=50, null=True, blank=True)
    big_search_title_text_color = models.CharField(max_length=50, null=True, blank=True)
    big_search_hyperlink_text_color = models.CharField(max_length=50, null=True, blank=True)
    big_search_search_icon_color = models.CharField(max_length=50, null=True, blank=True)

    # Datasets section
    datasets_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Datasets background")
    datasets_title_text_color = models.CharField(max_length=50, null=True, blank=True)
    datasets_icon_color = models.CharField(max_length=50, null=True, blank=True)
    datasets_icon_hover_color = models.CharField(max_length=50, null=True, blank=True)

    # Showcase section
    showcase_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_title_text_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_sub_text_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_icon_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_icon_title_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_icon_hover_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_button_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_button_text_color = models.CharField(max_length=50, null=True, blank=True)
    showcase_hyperlink_text_color = models.CharField(max_length=50, null=True, blank=True)

    # Footer section
    footer_bg = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Footer background")
    copyright_logo = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Copyright logo")

    # Primary button
    primary_button_color = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ("date",)
        verbose_name_plural = 'Advanced Themes'


# Disable other themes if one theme is enabled.
@receiver(post_save, sender=GeoNodeThemeCustomization)
@receiver(post_save, sender=AdvancedGeoNodeThemeCustomization)
def disable_other(sender, instance, **kwargs):
    if instance.is_enabled:
        AdvancedGeoNodeThemeCustomization.objects.exclude(pk=instance.pk).update(is_enabled=False)
        GeoNodeThemeCustomization.objects.exclude(pk=instance.pk).update(is_enabled=False)
