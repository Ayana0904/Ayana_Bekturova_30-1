"""
URL configuration for Blog01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static

from Blog01 import settings
from Product import views
from users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),

    path('products/', view.products_view),
    path('products/create/', views.product_create_view),
    path('posts/<int:id>/', views.post_detail_view),

    path('categories/', view.categories_view),

    path('users/reqister/', users_view.register_view),
    path('users/login/', users_view.login_view),
    path('users/logout/', users_view.logout_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
