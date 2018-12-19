# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import logging
import traceback

from django.contrib import messages
from django.contrib.admin import helpers
from django.template.response import TemplateResponse

from .models import AdvancedGeoNodeThemeCustomization

logger = logging.getLogger(__name__)


def enable_theme(self, request, queryset):
    """
    Activate the selected Themes
    """
    enabledThemes = AdvancedGeoNodeThemeCustomization.objects.filter(is_enabled=True).all()
    siteObjs = queryset.filter(is_enabled=False).all()
    if len(enabledThemes) > 0 or len(siteObjs) > 1:
        self.message_user(
            request,
            "Only one custom theme at once can be enabled. Disable current active custom theme to proceed!",
            level=messages.ERROR)
        return

    if request.POST.get("post"):
        for theme in siteObjs:
            try:
                """
                    Final checks if not exception has been raised until now
                """
                theme.is_enabled = True
                theme.save()
                self.message_user(request, "Enabled Theme: " + theme.name)
            except BaseException:
                self.message_user(
                    request,
                    "Exception occurred while trying to activate theme: " + theme.name,
                    level=messages.ERROR)
                tb = traceback.format_exc()
                self.message_user(
                    request,
                    tb,
                    level=messages.WARNING)
                logger.debug(tb)
                return
    else:
        context = {
            "objects_name": "Themes",
            'title': "Activate GeoNode Custom Themes",
            'action_exec': "enable_theme",
            'cancellable_themes': siteObjs,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return TemplateResponse(
            request,
            'admin/themes/confirm_cancel.html',
            context=context)


def disable_theme(self, request, queryset):
    """
    Disable the selected Themes
    """
    siteObjs = queryset.filter(is_enabled=True).all()
    if len(siteObjs) == 0:
        self.message_user(
            request,
            "Please select at least one active custom theme to disable!",
            level=messages.ERROR)
        return

    if request.POST.get("post"):
        for theme in siteObjs:
            try:
                """
                    Final checks if not exception has been raised until now
                """
                theme.is_enabled = False
                theme.save()
                self.message_user(request, "Disabled Theme: " + theme.name)
            except BaseException:
                self.message_user(
                    request,
                    "Exception occurred while trying to deactivate theme: " + theme.name,
                    level=messages.ERROR)
                tb = traceback.format_exc()
                self.message_user(
                    request,
                    tb,
                    level=messages.WARNING)
                logger.debug(tb)
                return
    else:
        context = {
            "objects_name": "Themes",
            'title': "Deactivate GeoNode Custom Themes",
            'action_exec': "disable_theme",
            'cancellable_themes': siteObjs,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return TemplateResponse(
            request,
            'admin/themes/confirm_cancel.html',
            context=context)


enable_theme.short_description = "Activate Theme"
disable_theme.short_description = "Disable Theme"