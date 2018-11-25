from django.urls import path
from . import views
from pages.views import MenuList,MList,ProfileView,ManageOrders,OrderDetail,ManageStudents,StudentProfile,ManageMenu,UpdateMenu,CreateMenu

urlpatterns = [
   # path('order/',MList.as_view(),name='order'),
   path('',MenuList.as_view(),name='home'),
   path('about/',views.about,name='about'),
   path('order/',views.placeorder,name='order'),

   # path('profile/',views.profile,name='profile'),
   path('profile/',ProfileView.as_view(),name='profile'),
   path('profile/<int:pk>',StudentProfile.as_view(),name='student_profile'),

   path('manage_order/',ManageOrders.as_view(),name='manage_order'),
   path('manage_menu/',ManageMenu.as_view(),name='manage_menu'),
   path('update_menu/<int:pk>',UpdateMenu.as_view(),name='update_menu'),
   path('create_menu/',CreateMenu.as_view(),name='create_menu'),



   path('order_detail/<int:pk>',OrderDetail.as_view(),name='order_detail'),
   path('manage_students/',ManageStudents.as_view(),name='manage_students'),

   # path('profile/<int:pk>',views.payfees,name='pay_amount'),



   path('ordernow/',views.placeorder,name='placeorder'),
   # path('login/',views.login,name='login'),
]
