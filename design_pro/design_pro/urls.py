
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('design.urls')),
]

urlpatterns += static(settings.STATIC_URL)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]