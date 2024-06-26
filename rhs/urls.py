from django.contrib import admin
from django.urls import path
from rhs.views import index,about, contact,menu, blog, blog_single, reservation,manage_menu,post_detail, contact_view
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
    path('reservation/', reservation, name='reservation'),
    path('manage_menu', manage_menu, name='manage_menu'),  # No need for separate add/edit paths
    path('edit/<int:menu_item_id>/', manage_menu, name='manage_menu'),
    path('<int:pk>/', post_detail, name='blog-single'),
    # path('', menu_list, name='menu_list'),  # Add this for the main list
    path('contact/', contact_view, name='contact'),

]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)