from django.contrib import admin
from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_admin, name='login'),
    path('kantha/', views.dashboard, name='dashboard'),
    path('users/', include("users.urls", namespace="users")),

]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)