# views.py
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import Movie, Favorite
from .forms import MovieForm, MovieSearchForm 
from django.http import HttpResponse


@login_required
def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            if request.user.is_superuser:  # Check if the user is admin
                form.save()
                return redirect('home')
            else:
                return redirect('home')  # Redirect to home if user is not admin
    else:
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})
def home(request):
    title_query = request.GET.get('title')
    movies = Movie.objects.all()
    if title_query:
        print(title_query)
        movies = movies.filter(title=title_query)
    
    return render(request, 'home.html', {'movies': movies})



def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})





@login_required
def add_to_favorite(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user

    # Check if the favorite already exists
    if Favorite.objects.filter(user=user, movie=movie).exists():
        return HttpResponse("This movie is already in your favorites.")

    # Add to favorites
    Favorite.objects.create(user=user, movie=movie)
    return redirect('movie_detail', movie_id=movie_id)


@login_required
def favorite_list(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user).select_related('movie')
    return render(request, 'favorites.html', {'favorites': favorites})
