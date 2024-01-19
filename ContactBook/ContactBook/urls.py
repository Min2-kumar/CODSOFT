from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.create_retrive, name='addshow'),
    path('update/<int:id>/',views.update_data, name='update'),
    path('delete/<int:id>/', views.delete_data, name="delete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
