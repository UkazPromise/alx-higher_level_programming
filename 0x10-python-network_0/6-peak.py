#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    if not list_of_integers:
        return None
    
    lo = 0
    hi = len(list_of_integers) - 1  # Adjusted upper bound
    mid = lo + (hi - lo) // 2  # Calculate mid point

    # Check if mid is a peak
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
       (mid == hi or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    
    # If mid is not a peak, recursively search in the appropriate direction
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])  # Search right
    else:
        return find_peak(list_of_integers[:mid])  # Search left
