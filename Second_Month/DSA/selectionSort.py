"""
1.set first element as minimum
2.compare minimum element with second element
3.If second element is smaller than minimum,assign second element as minimum
4.After each iteration,minimum is placed in the front of the unsort list.
"""
def selectionSort(array,size):
    for i in range(size):
        minimum_index = i#0
        for j in range(i+1,size):
            if array[j] < array[minimum_index]:
                minimum_index = j

        #swap
        # temp = array[i]
        # array[i] = array[minimum_index]
        # array[minimum_index] = temp
        array[i],array[minimum_index]  = array[minimum_index],array[i]

if __name__ == '__main__':
    data = [20,12,10,15,2]
    size = len(data)
    selectionSort(data,size)
    print("Sorted array in ascending order : ",data)