
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from items import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
