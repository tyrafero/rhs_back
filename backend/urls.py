from django.contrib import admin
from django.urls import path
from rhs import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rhs.urls'))
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)