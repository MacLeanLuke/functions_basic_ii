# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    list2 = []
    if len(list) < 2:
        return False
    else:
        for i in range(0, len(list)):
            if list[i] > list[1]:
                list2.append(list[i])

    print(len(list2))
    return list2

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

