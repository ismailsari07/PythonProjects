from typing import List, Sequence


def binary_search(data, number):
    begin_index = 0
    end_index = len(data) - 1
    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2
        midpoint_value = data[midpoint]

        if(midpoint_value == number):
            return midpoint
        elif midpoint_value > number:
            end_index = midpoint - 1
        elif midpoint_value < number:
            begin_index = midpoint + 1
    return None
list = [0,2,3,4,6,10,23,41,49,54,72,89,163,284,320]
print(binary_search(list, 10))
