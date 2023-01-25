def merge(arr: list, left: int, mid: int, right: int) -> list:
    arr1, arr2 = arr[left: mid], arr[mid: right]
    result = [None] * len(arr)
    index_arr1, index_arr2, index_result = 0, 0, 0
    while index_arr1 < len(arr1) and index_arr2 < len(arr2):
        if arr1[index_arr1] <= arr2[index_arr2]:
            result[index_result] = arr1[index_arr1]
            index_arr1 += 1
        else:
            result[index_result] = arr2[index_arr2]
            index_arr2 += 1
        index_result += 1
    while index_arr1 < len(arr1):
        result[index_result] = arr1[index_arr1]
        index_arr1 += 1
        index_result += 1
    while index_arr2 < len(arr2):
        result[index_result] = arr2[index_arr2]
        index_arr2 += 1
        index_result += 1
    return result


def merge_sort(arr: list, left: int, right: int) -> None:
    pass


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


test()