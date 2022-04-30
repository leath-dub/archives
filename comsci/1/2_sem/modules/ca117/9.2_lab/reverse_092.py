def reverse_list(arr) -> list:
    if arr:
        return reverse_list(arr[1:]) + arr[:1]
    return []
