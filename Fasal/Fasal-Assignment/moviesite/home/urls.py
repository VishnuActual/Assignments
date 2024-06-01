
from django.urls import path
from .views import home, movie_detail, create_movie, add_to_favorite, favorite_list
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('create-movie/', create_movie, name='create_movie'),
    path('movie/<int:movie_id>/add_to_favorite/', add_to_favorite, name='add_to_favorite'),
    path('favorites/', favorite_list, name='favorite_list'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
