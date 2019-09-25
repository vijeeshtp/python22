nums = [1,2,3,4,5,6,7,66 ,77,33,55]
i = 0
print (len (nums))
sum =0
while i <  len (nums) :
    i = i + 1
    if nums[i] % 2 ==0:
        continue
    sum =sum + nums [i]
    if sum  > 100 :
        break

print (sum)
