from configparser import ConfigParser
from django.shortcuts import render
import tmdbsimple as tmdb
import os

config = ConfigParser()
config.read('movies/config.cfg')
print(os.getcwd())
tmdb.API_KEY = config['tmdb']['API_KEY']

# Create your views here.
def home_page(request):
    query = str(request.GET.get('query', 'Frozen'))
    print(query)
    search_result = tmdb.Search().movie(query=query)['results']
    from pprint import pprint
    pprint([r['popularity'] for r in search_result])
    frontend = {"search_result": sorted(search_result, key=lambda x: x['popularity'], reverse=True)}
    return render(request, "movies/movie.html", frontend)


