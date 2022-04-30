def minimum(arr) -> int:
    if len(arr) == 1:
        return arr[0]
    elif arr[0] < minimum(arr[1:]):
        return arr[0]
    else:
        return minimum(arr[1:])
