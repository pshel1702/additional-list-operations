"""Additional List Practice

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""

def multiplication_table(n):
    """
    Returns a 2-D array containing an nxn multiplication table
    where n is the argument passed in
    """

    #use list comprehension to create the first row of the table
    #use list comprehension again in a for loop to create 
    #all the rows in the table

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

    #Start with sum = 0
    #Loop through the lists to find matches
    #If match is found, add the indices.
    #Return option with least list index sum 
    #If multiple matches are found with the same sum, return the list with no 
    #particular order requirement

    temp_sum = 0
    final_list=[]
    for i in range(len(list1)):
        j=0
        while j<len(list2) and (list1[i] != list2[j]):
            j+=1
        if temp_sum == 0 or temp_sum == i+j:
            temp_sum = i+j
            final_list.append(list1[i])
        elif (i+j) < temp_sum :
            temp_sum = i+j
            final_list[0] = list1[i]


    return final_list



def replace_elements(arr):
    """
    Replaces each element in arr with the greatest item among the elements to its right,
    and replace the last element with -1 since there are no elements to its right.
    For example [9,1,3,8] would turn into [9, 8, 8, -1].
    The input array arr will be modified and the function will return None.
    """

    

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