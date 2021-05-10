def largestRectangle(heights:[int]):
    current=prev=0
    min_height_bar=-1
    max_area=0
    while  prev<len(heights):
        min_height_bar=heights[prev]
        current=prev
        while current<len(heights):
            min_height_bar=min(heights[current],min_height_bar)
            area=(current-prev+1)*min_height_bar
            max_area=max(max_area,area)
            current+=1
        prev+=1
    return max_area

print(largestRectangle([5,5,1,7,1,1,5,2,7,6]))