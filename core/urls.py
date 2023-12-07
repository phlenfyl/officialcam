from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.conf import settings
from django.conf.urls.static import static
...

schema_view = get_schema_view(
   openapi.Info(
      title="MFM Cameroon API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
#    url='https://backendcam-64bo4zjn.b4a.run',
   public=True,
   permission_classes=(permissions.AllowAny,),
)

translang = i18n_patterns (
   path('', include('main.urls')),
   path('program/', include('program.urls')),
   path('sermon/', include('sermon.urls')),
)

urlpatterns = [
   # Needed for locale change
]

urlpatterns = translang + [
   path('i18n/', include('django.conf.urls.i18n')),
   path('admin/', admin.site.urls),

   path('api', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('ckeditor/', include('ckeditor_uploader.urls')),
]





if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root= settings.COMPRESS_ROOT)

   urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
