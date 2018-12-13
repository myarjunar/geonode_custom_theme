# coding=utf-8
import os
import sys
import importlib


# Load default settings file from geonode
try:
    from geonode_custom_theme.local_settings import *
except ImportError:
    # Load from current settings file
    settings_file = os.environ.get(
        'DJANGO_SETTINGS_MODULE', 'geonode.settings')
    if settings_file not in sys.modules:
        current_settings = importlib.import_module(settings_file)
        sys.modules[settings_file] = current_settings
    else:
        current_settings = sys.modules[settings_file]

    locals().update(
        {
            k: getattr(current_settings, k)
            for k in dir(current_settings) if not k.startswith('_')
        })

PROJECT_NAME = 'geonode_custom_theme'

if PROJECT_NAME not in INSTALLED_APPS:
    INSTALLED_APPS += (PROJECT_NAME, )

# Location of url mappings
ROOT_URLCONF = os.getenv('ROOT_URLCONF', '{}.urls'.format(PROJECT_NAME))

WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)

# Defines the directory that contains the settings file as the _LOCAL_ROOT
# It is used for relative settings elsewhere.
_LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', "en")

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(_LOCAL_ROOT, "static"),
)

_LOCALE_DIR = os.path.join(_LOCAL_ROOT, 'locale')
_TEMPLATE_DIR = os.path.join(_LOCAL_ROOT, 'templates')

# Prioritize custom translations
LOCALE_PATHS = list(LOCALE_PATHS)
LOCALE_PATHS.insert(0, _LOCALE_DIR)

# Prioritize custom theme
template_dirs = list(TEMPLATES[0]['DIRS'])
template_dirs.insert(0, _TEMPLATE_DIR)

TEMPLATES[0]['DIRS'] = template_dirs

# Add custom template context processors
context_processors = list(TEMPLATES[0]['OPTIONS']['context_processors'])
context_processors += ['geonode_custom_theme.context_processors.custom_theme']

TEMPLATES[0]['OPTIONS']['context_processors'] = context_processors
