from django.contrib import admin
from django.urls import path
from rhs.views import index,about, contact,menu, blog, blog_single, reservation,manage_menu
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('menu/', menu, name='menu'),
    path('blog/', blog, name='blog'),
    path('blog-single/', blog_single, name='blog-single'),
    path('reservation/', reservation, name='reservation'),
    path('manage_menu', manage_menu, name='manage_menu'),  # No need for separate add/edit paths
    path('edit/<int:menu_item_id>/', manage_menu, name='manage_menu'),
    # path('', menu_list, name='menu_list'),  # Add this for the main list

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)