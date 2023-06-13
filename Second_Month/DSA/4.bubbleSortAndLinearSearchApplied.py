def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

# def linear_search(numbers,target_number):
#     for number in numbers:
#         if number == target_number:
#             return True
#     return False

def linear_search(numbers,target_number):
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            return i
    return -1

if __name__ == '__main__':
    numbers_list = [5,2,8,1,3,9]
    target_number = int(input("Enter your number to search: "))
    bubble_sort(numbers_list)
    print("After sorting list: ",numbers_list)
    is_found = linear_search(numbers_list,target_number)
    # if is_found:
    #     print(f'The number {target_number} is found in the list!')
    # else:
    #     print(f'The number {target_number} is not found in the list!')

    if is_found != -1:
        print(f'The number {target_number} is found in the list of index {is_found}!')
    else:
        print(f'The number {target_number} is not found in the list!')