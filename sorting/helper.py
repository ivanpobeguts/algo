import traceback
import sys

__author__ = 'Ivan Pobeguts'

def swap(array, left, right):
    if left != right:
        temp = array[right]
        array[right] = array[left]
        array[left] = temp

