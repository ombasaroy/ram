
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/', views.product, name='product'),
    path('ramadmin/', views.ramadmin, name='ramadmin'),
    path('ramadmin-login/', views.ramadmin_login, name='ramadmin_login'),
    path('ramadmin-register/', views.ramadmin_register, name='ramadmin_register'),
    path('ramadmin-add-product/', views.ramadmin_add_product, name='ramadmin_add_product'),
    path('ramadmin-add-category/', views.ramadmin_add_category, name='ramadmin_add_category'),
    path('ramadmin-categories/', views.ramadmin_categories, name='ramadmin_categories'),

]
