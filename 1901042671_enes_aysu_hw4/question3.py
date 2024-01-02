value_arr = [3, 1, -2, 1, -1, -2, 4, -2, 1, 2]

# initialize values
first = 0
second = 1
largest = value_arr[0]

# finds sum of between first and second intervals
def sum_of_intervals(arr, first, second):
    if first == second:
        return arr[first]
    else:
        return arr[first] + sum_of_intervals(arr, first + 1, second)
    
# recursive function that finds largest interval area   
def find_largest_area(value_arr, largest, first, second):
    if second == len(value_arr) and first == len(value_arr) - 1:
        # if it reachs the end returns largest area
        return largest
    
    temp = sum_of_intervals(value_arr, first, second)

    if second == len(value_arr) - 1:
        first += 1
        second = first

    if temp > largest:
        largest = temp  

    return find_largest_area(value_arr, largest, first, second + 1) 

print("maximum largest area:", find_largest_area(value_arr, largest, first, second))        

       
