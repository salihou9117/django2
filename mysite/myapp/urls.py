from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    path("contact/", views.contact, name="contact"),
    path("cart", views.cart, name="cart"),
    path("product/", views.product, name="product"),
]
