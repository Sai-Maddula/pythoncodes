def find_duplicate_elem(arr):
    prev=-1
    i=0
    visited = set()
    for i in range(len(arr)):
        if arr[i] in visited:
            print(arr[i])
            break
        visited.add(arr[i])

find_duplicate_elem([1,2,3,3,45])