from helper import swap

__author__ = 'Ivan Pobeguts'


def insertion_sort(list_to_sort):
    step = 0
    for i in range(1, len(list_to_sort)):
        position = i
        current_value = list_to_sort[i]
        while position > 0 and list_to_sort[position - 1] > current_value:
            swap(list_to_sort, position - 1, position)
            position = position - 1
            print('Step {}: {}'.format(step, list_to_sort))
            step += 1


if __name__ == '__main__':
    list_to_sort = [3, 7, 4, 4, 6, 5, 8, 2, 10, 98, 9, 24, 1]
    print('Insertion sort')
    print('-' * 50)
    print('Unsorted list: ', list_to_sort)
    insertion_sort(list_to_sort)
    print('Sorted list: ', list_to_sort)
