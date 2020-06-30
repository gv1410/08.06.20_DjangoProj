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
from testapp.views import homepage, ListWriter,CreateWriter, test, UserLogOutView, UserRegistrView, UserLoginView, CreateGenre, CreateBook, UpdateGenre, ListGenre, DeleteGenre, UpdateBook, ListBook, DeleteBook, DetailBook, DetailGenre, HomepageList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path('listgenre/', ListGenre.as_view(), name='listgenre'),
    path('creategenre/', CreateGenre.as_view(), name='creategenre'),
    path('<int:id>/updategenre/', UpdateGenre.as_view(), name='updategenre'),
    path('<int:pk>/deletegenre/', DeleteGenre.as_view(), name='deletegenre'),
    path('listbook/', ListBook.as_view(), name='listbook'),
    path('createbook/', CreateBook.as_view(), name ='createbook'),
    path('<int:id>/updatebook/', UpdateBook.as_view(), name='updatebook'),
    path('<int:pk>/deletebook/', DeleteBook.as_view(), name='deletebook'),
    path('<int:pk>/detailbook/', DetailBook.as_view(), name='detailbook'),
    path('<int:pk>/detailgenre/', DetailGenre.as_view(), name='detailgenre'),
    path('homepage/', HomepageList.as_view(), name ='homepage'),
    path('login/', UserLoginView.as_view(), name ='login'),
    path('register/', UserRegistrView.as_view(), name ='register'),
    path('logout/', UserLogOutView.as_view(), name ='logout'),
    path('', homepage, name ='home'),
    path('createwriter/', CreateWriter.as_view(), name ='createwriter'),
    path('listwriter/', ListWriter.as_view(), name ='listwriter'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
