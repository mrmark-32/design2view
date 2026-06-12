from django.contrib import admin
from django.urls import path
from django.conf import settings             # <-- IMPORT THIS
from django.conf.urls.static import static   # <-- IMPORT THIS
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),

    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    path('category/<slug:category_slug>/fabric/<int:fabric_id>/', views.fabric_detail, name='fabric_detail'),
    
]

# Append media file URL routing for local development testing
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)