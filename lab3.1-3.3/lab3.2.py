# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep = ','):
    firstS = first.split(sep)
    secondS = second.split(sep)
    firstSS = set(firstS)
    secondSS = set(secondS)
    common = list(firstSS.intersection(secondSS))
    common.sort()
    return  common

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print('Общие участники:', find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
