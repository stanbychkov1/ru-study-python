class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if len(input_list) == 0:
            return input_list

        new_list = sorted(list(set(input_list)))
        max_item = new_list[-1]

        for index, item in enumerate(input_list):
            if item >= 0:
                input_list[index] = max_item

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        def inner(first, last):

            match len(input_list[first: last+1]):
                case 0:
                    return -1

            mid = (first + last) // 2
            item = input_list[mid]

            if query == item:
                return mid
            elif query > item:
                return inner(mid+1, last)
            else:
                return inner(first, mid-1)

        return inner(0, len(input_list)-1)
