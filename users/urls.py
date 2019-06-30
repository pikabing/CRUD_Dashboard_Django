from django.contrib import admin
from django.urls import path
from . import views 


app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userlist, name='list'),
    path('pending/', views.userinactivelist, name='pending'),
    path('list/', views.userlist, name='active'),
    path('active/<int:id>', views.makeactive, name='makeactive'),
    path('inactive/<int:id>', views.makeinactive, name='makeinactive'),
    path('edit/<int:id>', views.edituser, name='edit'),
    path('edit/type/<str:value>', views.get_type, name='type'),
    path('update/<int:pk>', views.update, name='update'),
    path('detail/<int:pk>', views.UserDetail.as_view(), name='detail'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='delete'),
    path('relation/<int:pk>', views.addrelation, name='relation'),
    path('relation/usersautocomp/', views.get_user_auto, name='autocomp'),
    path('relation/add/<int:id>', views.user_relation, name='addrelation'),
] 
