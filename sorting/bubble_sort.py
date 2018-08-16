__author__ = 'Ivan Pobeguts'


def swap(array, left, right):
    if left != right:
        temp = array[right]
        array[right] = array[left]
        array[left] = temp


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
    ARRAY = [3, 7, 4, 4, 6, 5, 8, 3, 5, 7, 2, 1, 5, 9]
    print('Bubble sort')
    print('-' * 50)
    print('Unsorted array: ', ARRAY)
    bubble_sort(ARRAY)
    print('Sorted array: ', ARRAY)
