def reverseArray(arr):
    return arr[::-1]

#Stretch goal
def reverseArray(arr):
    for i in range(len(arr)):
        arr[i], arr[-i -1] = arr[-i-1], arr[i]
    return arr
