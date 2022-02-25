from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Tool


# Create your views here.
def index(request):
    movies = Tool.objects.all()
    # output = ', '.join([m.title for m in movies])

    # SELECT * From movies_movie
    # Movie.objects.filter(release_year=1984)
    # # SELECT * FROM movies_movie WHERE
    # Movie.objects.get(id=1)

    # return HttpResponse("Hello world")

    # return HttpResponse(output)

    return render(request, 'tools/index.html', {'tools': movies})


def detail(request, movie_id):

    movie = get_object_or_404(Tool, pk=movie_id)
    # return HttpResponse(movie_id)

    return render(request, 'tools/detail.html', {'tool': movie})
