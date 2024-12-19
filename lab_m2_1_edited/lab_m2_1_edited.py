import doctest

class Book:
    def __init__(self, total_pages: int, current_page: int = 0):
        """
        Создание и подготовка к работе объекта "Книга"

        :param total_pages: Общее количество страниц в книге
        :param current_page: Текущая страница, на которой находится читатель
        Примеры:
        >>> book = Book(300)  # инициализация экземпляра класса
        >>> book.total_pages
        300
        >>> book.current_page
        0
        """
        if not isinstance(total_pages, int):
            raise TypeError("Общее количество страниц должно быть типа int")
        if total_pages <= 0:
            raise ValueError("Общее количество страниц должно быть положительным числом")

        self.total_pages = total_pages

        if not isinstance(current_page, int):
            raise TypeError("Текущая страница должна быть типа int")
        if current_page < 0 or current_page > total_pages:
            raise ValueError("Текущая страница должна быть в пределах от 0 до общего количества страниц")

        self.current_page = current_page

    def is_book_finished(self) -> bool:
        """
        Проверяет, закончена ли книга.

        :return: Является ли книга прочитанной

        Примеры:
        >>> book = Book(300)
        >>> book.is_book_finished()
        False
        >>> book2 = Book(300, 300)
        >>> book2.is_book_finished()
        True
        """
        return self.current_page == self.total_pages

    def turn_page(self) -> None:
        """
        Переход на следующую страницу.

        :raise ValueError: Если текущая страница уже последняя, вызываем ошибку.

        Примеры:
        >>> book = Book(300)
        >>> book.turn_page()
        >>> book.current_page
        1
        >>> for _ in range(299):  # переходим на последнюю страницу
        ...     book.turn_page()
        >>> book.turn_page()  # это должно вызвать ошибку
        Traceback (most recent call last):
            ...
        ValueError: Вы уже на последней странице книги
        """
        if self.current_page >= self.total_pages:
            raise ValueError("Вы уже на последней странице книги")

        self.current_page += 1

    def go_to_page(self, page: int) -> None:
        """
        Переход на указанную страницу.

        :param page: Номер страницы, на которую нужно перейти
        :raise ValueError: Если номер страницы вне допустимого диапазона, вызываем ошибку.

        Примеры:
        >>> book = Book(300)
        >>> book.go_to_page(150)
        >>> book.current_page
        150
        >>> book.go_to_page(301)  # это должно вызвать ошибку
        Traceback (most recent call last):
            ...
        ValueError: Номер страницы должен быть в пределах от 0 до 300
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть типа int")

        if page < 0 or page > self.total_pages:
            raise ValueError(f"Номер страницы должен быть в пределах от 0 до {self.total_pages}")

        self.current_page = page



class Movie:
    def __init__(self, total_duration: int, current_time: int = 0):
        """
        Создание и подготовка к работе объекта "Фильм"
        :param total_duration: Общая продолжительность фильма в минутах
        :param current_time: Текущее время просмотра в минутах
        Примеры:
        >>> movie = Movie(120)  # инициализация экземпляра класса
        >>> movie.total_duration
        120
        >>> movie.current_time
        0
        """
        if not isinstance(total_duration, int):
            raise TypeError("Общая продолжительность должна быть типа int")
        if total_duration <= 0:
            raise ValueError("Общая продолжительность должна быть положительным числом")
        self.total_duration = total_duration
        if not isinstance(current_time, int):
            raise TypeError("Текущее время должно быть типа int")
        if current_time < 0 or current_time > total_duration:
            raise ValueError("Текущее время должно быть в пределах от 0 до общей продолжительности")
        self.current_time = current_time

    def is_movie_finished(self) -> bool:
        """
        Проверяет, закончен ли фильм.
        :return: Является ли фильм просмотренным
        Примеры:
        >>> movie = Movie(120)
        >>> movie.is_movie_finished()
        False
        >>> movie2 = Movie(120, 120)
        >>> movie2.is_movie_finished()
        True
        """
        return self.current_time == self.total_duration

    def watch_minutes(self, minutes: int) -> None:
        """
        Просмотр указанного количества минут.
        :param minutes: Количество минут для просмотра
        :raise ValueError: Если текущее время превышает общую продолжительность, вызываем ошибку.
        Примеры:
        >>> movie = Movie(120)
        >>> movie.watch_minutes(30)
        >>> movie.current_time
        30
        >>> movie.watch_minutes(100)  # это должно вызвать ошибку
        Traceback (most recent call last):
        ...
        ValueError: Вы уже просмотрели весь фильм
        """
        if not isinstance(minutes, int):
            raise TypeError("Количество минут должно быть типа int")

        if self.current_time + minutes > self.total_duration:
            raise ValueError("Вы уже просмотрели весь фильм")

        self.current_time += minutes



class AudioBook:
    def __init__(self, total_duration: int, current_time: int = 0):
        """
        Создание и подготовка к работе объекта "Аудиокнига"
        :param total_duration: Общая продолжительность аудиокниги в минутах
        :param current_time: Текущее время прослушивания в минутах
        Примеры:
        >>> audiobook = AudioBook(360)  # инициализация экземпляра класса
        >>> audiobook.total_duration
        360
        >>> audiobook.current_time
        0
        """
        if not isinstance(total_duration, int):
            raise TypeError("Общая продолжительность должна быть типа int")
        if total_duration <= 0:
            raise ValueError("Общая продолжительность должна быть положительным числом")

        self.total_duration = total_duration

        if not isinstance(current_time, int):
            raise TypeError("Текущее время должно быть типа int")

        if current_time < 0 or current_time > total_duration:
            raise ValueError("Текущее время должно быть в пределах от 0 до общей продолжительности")

        self.current_time = current_time

    def is_audiobook_finished(self) -> bool:
        """
        Проверяет, закончена ли аудиокнига.
        :return: Является ли аудиокнига прослушанной
        Примеры:
        >>> audiobook = AudioBook(360)
        >>> audiobook.is_audiobook_finished()
        False
        >>> audiobook2 = AudioBook(360, 360)
        >>> audiobook2.is_audiobook_finished()
        True
        """
        return self.current_time == self.total_duration

    def listen_minutes(self, minutes: int) -> None:
        """
        Прослушивание указанного количества минут.
        :param minutes: Количество минут для прослушивания
        :raise ValueError: Если текущее время превышает общую продолжительность, вызываем ошибку.
        Примеры:
        >>> audiobook = AudioBook(360)
        >>> audiobook.listen_minutes(60)
        >>> audiobook.current_time
        60
        >>> audiobook.listen_minutes(300)  # это должно вызвать ошибку
        Traceback (most recent call last):
        ...
        ValueError: Вы уже прослушали всю аудиокнигу
        """
        if not isinstance(minutes, int):
            raise TypeError("Количество минут должно быть типа int")

        if self.current_time + minutes > self.total_duration:
            raise ValueError("Вы уже прослушали всю аудиокнигу")

        self.current_time += minutes


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
