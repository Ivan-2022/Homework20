from unittest.mock import MagicMock
import pytest
from dao.model.director import Director
from dao.director import DirectorDAO
from dao.model.genre import Genre
from dao.genre import GenreDAO
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    jonh = Director(id=1, name='jonh')
    kate = Director(id=2, name='kate')
    maxim = Director(id=3, name='maxim')  # для добавления нового режиссера

    director_dao.get_one = MagicMock(return_value=jonh)
    director_dao.get_all = MagicMock(return_value=[jonh, kate])
    director_dao.create = MagicMock(return_value=maxim)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='comedy')
    family = Genre(id=2, name='family')
    fantasy = Genre(id=3, name='fantasy')  # для добавления нового жанра

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, family])
    genre_dao.create = MagicMock(return_value=fantasy)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='movie_1', description='description', trailer='trailer_1', year=2020, rating=3)
    movie_2 = Movie(id=2, title='movie_2', description='description', trailer='trailer_2', year=2021, rating=4)
    movie_3 = Movie(id=3, title='movie_3', description='description', trailer='trailer_3', year=2022, rating=5)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=movie_3)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao
