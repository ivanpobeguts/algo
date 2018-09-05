__author__ = 'Ivan Pobeguts'


def merge(left_sublist, right_sublist):
    i, j = 0, 0
    result = []
    while i < len(left_sublist) and j < len(right_sublist):
        # if left value is lower than right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            # if right value is lower than left then append it to the result
            result.append(right_sublist[j])
            j += 1
    # concatenate the rest of the left and right sublists
    result += left_sublist[i:]
    result += right_sublist[j:]
    # return the result
    return result


def merge_sort(list):
    if len(list) < 2:
        return list
    mid = int(len(list) / 2)
    a = merge_sort(list[:mid])
    b = merge_sort(list[mid:])
    return merge(a, b)


if __name__ == '__main__':
    list_to_sort = [3, 7, 4, 4, 6, 5, 8, 2, 10, 98, 9, 24, 1]
    print('Merge sort')
    print('-' * 50)
    print('Unsorted list: ', list_to_sort)
    print('Sorted list: ', merge_sort(list_to_sort))
