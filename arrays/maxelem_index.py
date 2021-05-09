def MaxInArray(arr):
    print(max(arr))
    print(arr.index(max(arr)))

def CardsPyramid(n):
    if n ==0:
        return -1
    cards = int(n*(3*n+1)/2)
    return int(cards%1000007)

print(CardsPyramid(3))
MaxInArray([23,45,82,27,66,12,78,12,71,86])