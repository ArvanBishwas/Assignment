from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from ideas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('accounts/', include('accounts.urls')),
    path('ideas/',include('ideas.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
