from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView, name='Home'),
    path('movielist/', MovieList, name='movielist'),
    path('booksite/', booksite, name='booksite'),
    path('movie-detail-<int:id>/', MovieDetail, name='MovieDetail'),
    path('register/', UserRegistionView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)