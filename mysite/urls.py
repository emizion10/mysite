from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
  # path('login/',auth_views.Login,name='login'),
   # path('logout/',auth_views.Logout,name='logout'),
   	path('acc/',include('django.contrib.auth.urls')),
    path('',include('pages.urls')),
]

