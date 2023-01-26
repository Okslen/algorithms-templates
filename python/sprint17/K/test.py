arr1 = [5, 2]
arr2 = [3, 4]
arr1.extend(arr2)
print(arr1)

def sorting(arr):
    arr.clear()
    arr.extend(arr1)


sorting(arr1)
print(arr1)