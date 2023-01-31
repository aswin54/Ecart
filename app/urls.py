from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tailor_register',views.tailor_register,name='tailor_register'),
    path('tailor_view',views.tailor_view,name='tailor_view'),
]