from functools import reduce
from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        filtered_list = filter(lambda movie:
                               movie['rating_kinopoisk']
                               and float(movie['rating_kinopoisk']) > 0
                               and movie['country'].count(',') >= 1,
                               list_of_movies)
        rating_list = list(map(lambda rating:
                               float(rating['rating_kinopoisk']),
                               filtered_list))
        average_rating = reduce(lambda accum, rating:
                                accum + rating,
                                rating_list) / len(rating_list)

        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict],
                    rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        filtered_list = filter(lambda movie:
                               movie['rating_kinopoisk']
                               and float(movie['rating_kinopoisk']) > rating,
                               list_of_movies)
        counted_list = list(map(lambda symbol_quantity:
                                symbol_quantity['name'].count('и'),
                                filtered_list))
        if len(counted_list) == 0:
            return 0
        return reduce(lambda accum, quantity:
                      accum + quantity,
                      counted_list)
