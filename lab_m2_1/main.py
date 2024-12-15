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


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации