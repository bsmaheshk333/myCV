from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about-author"),


    path('download-pdf/', views.export_pdf, name="download_pdf"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout")
]

# for media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# For static files css/html/js
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

