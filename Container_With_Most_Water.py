def maxArea(heights:[int]):
    def calculateArea(height,left,right):
        return (right-left)*min(height[left],height[right])
    left=0
    right=len(heights)-1
    max_water=0
    while left<right:
        max_water=max(max_water,calculateArea(heights,left=left,right=right))
        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return max_water   
        
        
    
        

print(maxArea([1,8,6,2,5,4,8,3,7]))