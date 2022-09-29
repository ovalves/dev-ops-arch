from django.conf import settings

if not settings.configured:
    settings.configure(USE_I18N=False)
