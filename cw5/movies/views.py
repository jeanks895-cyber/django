from django.shortcuts import render
from .forms import MovieForm

def index(request):
    success_message = None
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            success_message = f"Movie saved: {movie.name} ({movie.release_year})"
            form = MovieForm() # Reset the form after successful submission
    else:
        form = MovieForm()
        
    return render(request, 'movies/index.html', {'form': form, 'success_message': success_message})
