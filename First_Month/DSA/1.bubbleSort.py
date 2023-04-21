def bubbleSort(data):
    for i in range(len(data)):
        for j in range(0,len(data)-i-1):#5-2-1=2 , j=0,1
            if data[j] > data[j+1]:
                #swapping elements
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

if __name__ == "__main__":
    data  = [-2,45,0,11,-9]
    bubbleSort(data)
    print('Sorted Array in Ascending order',data)