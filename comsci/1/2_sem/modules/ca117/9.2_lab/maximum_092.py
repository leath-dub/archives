def maximum(arr) -> int:
    if len(arr) == 1:
        return arr[0]
    elif arr[0] > maximum(arr[1:]):
        return arr[0]
    else:
        return maximum(arr[1:])
