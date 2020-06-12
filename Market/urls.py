"""Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import registerPage,loginPage
from products.views import registerProductPage,productListPage,productPage,productCartPage,cartPage
from django.views.generic import RedirectView

urlpatterns = [
    path('products/cart', cartPage, name="Cart"),
    path('products/list/<int:id>/added', productCartPage, name="ProductCart"),
    path('products/list/<int:id>/', productPage, name="Product"),
    path('products/list/', productListPage, name="ProductList"),
    path('', RedirectView.as_view(url='/products/list')),
    path('products/register/', registerProductPage, name="Register"),
    path('auth/login/', loginPage, name="Login"),
    path('auth/register/', registerPage, name="Sign Up"),
    path('admin/', admin.site.urls),
]
