def shell_sort(arr):
    arr = arr[:]
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


if __name__ == "__main__":
    print(shell_sort([5, 3, 8, 4, 2]))
