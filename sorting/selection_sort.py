from helper import swap

__author__ = 'Ivan Pobeguts'


def selection_sort(list_to_sort):
    step = 0
    for i in range(0, len(list_to_sort)):
        min = i
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min]:
                min = j
        swap(list_to_sort, min, i)
        print('Step {}: {}'.format(step, list_to_sort))
        step += 1


if __name__ == '__main__':
    list_to_sort = [3, 7, 4, 4, 6, 5, 8, 2, 10, 98, 9, 24, 1]
    print('Selection sort')
    print('-' * 50)
    print('Unsorted list: ', list_to_sort)
    selection_sort(list_to_sort)
    print('Sorted list: ', list_to_sort)
