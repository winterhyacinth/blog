from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>", views.detail, name="detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)