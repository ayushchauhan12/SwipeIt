from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('profile',views.profile,name="profile"),
    path('tokens',views.tokens,name="tokens"),
    path('orders',views.orders,name="orders"),
    path('rewards',views.rewards,name="rewards"),
    path('redeem', views.redeem, name="redeem"),
    path('confirmredeem/', views.confirmredeem, name="cnfrmredeem"),
    path('checkout/', views.checkout, name="Checkout"),

]
