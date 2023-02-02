from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tailor_register',views.tailor_register,name='tailor_register'),
    path('tailor_view',views.tailor_view,name='tailor_view'),
    path('tailor_edit/<int:id>',views.tailor_edit,name='tailor_edit'),
    path('tailor_delete/<int:id>',views.tailor_delete,name='tailor_delete'),
    path('dresscategory_add',views.dresscategory_add,name='dresscategory_add'),
    path('dresscategory_view',views.dresscategory_view,name='dresscategory_view'),
    path('dresscategory_delete/<int:id>',views.dresscategory_delete,name='dresscategory_delete'),
]