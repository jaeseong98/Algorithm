def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    # pivot value 기준 왼쪽 영역 arr은 pivot value 보다 작은 arr가 되고
    # pivot value 기준 오른쪽 영역은 pivot value 보다 큰 arr가 된다.
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

arr = [1,2,5,4,3]

print(quick_sort(arr))
