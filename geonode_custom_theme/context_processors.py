from .models import AdvancedGeoNodeThemeCustomization
from geonode.client.models import GeoNodeThemeCustomization

def custom_theme(request):
    try:
        theme = AdvancedGeoNodeThemeCustomization.objects.get(is_enabled=True)
    except AdvancedGeoNodeThemeCustomization.DoesNotExist:
        try:
            theme = GeoNodeThemeCustomization.objects.get(is_enabled=True)
        except GeoNodeThemeCustomization.DoesNotExist:
            theme = {}
    return {'custom_theme': theme}
