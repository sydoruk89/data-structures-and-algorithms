# Array Shift 
def insertShiftArray(arr, el):
    index = 0
    if len(arr) % 2 == 0:
        index = len(arr)//2
    else:
        index = len(arr) // 2 + 1
    print(index)
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    new_arr.append(el)
    for i in range(index, len(arr)):
        new_arr.append(arr[i])    
    return new_arr

print(insertShiftArray([1, 2, 3, 5, 6], 4))
