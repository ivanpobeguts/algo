import traceback
import sys

__author__ = 'Ivan Pobeguts'


def swap(array, left, right):
    if left != right:
        array[right], array[left] = array[left], array[right]

def swap1(left, right):
    if left > right:
        right, left = left, right
