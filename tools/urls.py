from django.urls import path
from . import views


# movies/
# movies/1
urlpatterns = [
    path('', views.index, name='tools_index'),
    path('<int:movie_id>', views.detail, name='tools_detail')
]
