from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls")),
    path('tinymce/', include('tinymce.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "HAMD Shipping Administration"
admin.site.site_title = "HAMD Shipping Admin Portal"
admin.site.index_title = "Welcome to HAMD Shipping Admin Portal"