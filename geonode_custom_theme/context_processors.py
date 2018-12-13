from .models import AdvancedGeoNodeThemeCustomization

def custom_theme(request):
    try:
        theme = AdvancedGeoNodeThemeCustomization.objects.get(is_enabled=True).all()
    except AdvancedGeoNodeThemeCustomization.DoesNotExist:
        theme = {}
    return {'custom_theme': theme}
