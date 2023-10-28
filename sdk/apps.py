from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SDKConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sdk"
    verbose_name = _("Riso SDK")
