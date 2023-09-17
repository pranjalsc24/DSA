# ------ using inbuild library----

# ------logical way--------

def min_max(nums):
    arr=nums[0]

    for i in range (len(nums)):
        if nums[i] > arr:
            max=nums[i]
    print(max)

    for i in range (len(nums)):
        if nums[i] < arr:
            min=nums[i]
    print(min)


min_max([2,7,4,9,5,1,78,90])



# using recursion
             
