from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from views import index

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", index, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^accounts/", include("account.urls")),
    url(r"^surveys/", include("formly.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
