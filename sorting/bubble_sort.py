from helper import swap

__author__ = 'Ivan Pobeguts'


def bubble_sort(ARRAY):
    sorted = False
    step = 0
    while not sorted:
        sorted = True
        for i in range(0, len(ARRAY) - 1):
            if ARRAY[i] > ARRAY[i + 1]:
                sorted = False
                swap(ARRAY, i, i + 1)
                print('Step {}: {}'.format(step, ARRAY))
                step += 1


if __name__ == '__main__':
    ARRAY = [3, 7, 4, 4, 6, 5, 8, 2, 10, 98, 9, 24, 1]
    print('Bubble sort')
    print('-' * 50)
    print('Unsorted array: ', ARRAY)
    bubble_sort(ARRAY)
    print('Sorted array: ', ARRAY)
