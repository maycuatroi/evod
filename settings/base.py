from django.conf import settings
from django.test.signals import setting_changed

EVOD_APPS = [
    'django_firebase_auth'
]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "django_firebase_auth.firebase_auth.FirebaseAuthentication",
    ),
}


def merge_installed_apps(new_apps):
    settings.INSTALLED_APPS = list(settings.INSTALLED_APPS)
    for app in new_apps:
        if app not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS.append(app)


def set_installed_apps(new_apps: list):
    merge_installed_apps(new_apps)
    setting_changed.send(sender=__name__, setting='INSTALLED_APPS', value=new_apps, enter=True)


set_installed_apps(EVOD_APPS)
