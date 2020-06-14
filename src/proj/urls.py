"""proj URL Configuration

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
from django.urls import path, include
from testapp.views import test, CreateGenre, CreateBook, UpdateGenre, ListGenre, DeleteGenre, UpdateBook, ListBook, DeleteBook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path('creategenre/', CreateGenre.as_view(), name='creategenre'),
    path('createbook/', CreateBook.as_view(), name ='createbook'),
    path('<int:id>/updategenre/', UpdateGenre.as_view(), name='updategenre'),
    path('listgenre/', ListGenre.as_view(), name='listgenre'),
    path('<int:pk>/deletegenre/', DeleteGenre.as_view(), name='deletegenre'),
    path('<int:id>/updatebook/', UpdateBook.as_view(), name='updatebook'),
    path('listbook/', ListBook.as_view(), name='listbook'),
    path('<int:pk>/deletebook/', DeleteBook.as_view(), name='deletebook'),
]
