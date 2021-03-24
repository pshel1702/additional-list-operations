"""Additional List Practice

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""

def multiplication_table(n):
    """
    Returns a 2-D array containing an nxn multiplication table
    where n is the argument passed in
    """

    #create a new list
    #every element in the list will be multiplied by the current index of the loop
    mult_table = []
    orig_table = [1*num for num in range(1,n+1)]
    row = []

    for i in range (1,n+1):
        row = [i * index_val for index_val in orig_table]
        mult_table.append(row)
    
    return mult_table


def find_common_items_minimum_index_sum(list1, list2):
    """
    Returns the common item(s) between the two lists which have the lowest index sum
    (the sum of the index of the item in each list.) If there is a tie, return all
    items with the lowest index sum.
    """
    sum = 0
    final_list=[]
    for i in range (len(list1)):
        temp_sum = 0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                temp_sum = i+j
                if sum == 0:
                    sum = temp_sum
                    final_list.append(list1[i])
                elif temp_sum == sum:
                    final_list.append(list1[i])

    return final_list



def replace_elements(arr):
    """
    Replaces each element in arr with the greatest item among the elements to its right,
    and replace the last element with -1 since there are no elements to its right.
    For example [9,1,3,8] would turn into [9, 8, 8, -1].
    The input array arr will be modified and the function will return None.
    """

    # TODO: replace this with your code

def add_to_array_form(array_form_of_number, integer_to_add):
    """
    For a non-negative integer N, the array-form of N is an array of its digits in left to right order.
    Takes the array-form of a non-negative integer (`array_form_of_number`) as well as an integer to add to it (`integer_to_add`) and returns the array-form of their sum.
    """

    # TODO: replace this with your code

if __name__ == "__main__":
    from pathlib import Path
    import sys
    import pytest

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([f"test_{Path(__file__).name}"])