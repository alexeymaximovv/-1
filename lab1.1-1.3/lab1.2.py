volume_Mb = 1.44
pages = 100
lines = 50
symb = 25
#1 symb = 4 bites

volume1book_b = symb * lines * pages
volume1book_Kb = volume1book_b / 1024
volume1book_Mb = round(volume1book_Kb / 1024, 2)

books = volume_Mb // volume1book_Mb

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books)
