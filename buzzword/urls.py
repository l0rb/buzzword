from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from buzzword.user_admin_page import user_admin

urlpatterns = [
    path("", include("start.urls")),
    path("", include("accounts.urls")),
    path("explore/", include("explore.urls")),
    path("admin/", admin.site.urls),
    path("settings/", user_admin.urls),
    path("resources/", include("django_plotly_dash.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
