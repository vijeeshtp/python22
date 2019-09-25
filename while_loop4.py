i = 1
even_sum = 0
odd_sum = 0
while i <= 10 :
    s = "Enter " + str (i)  + " th Number :"
    num = int (input (s))
    if (num%2==0):
        even_sum = even_sum + num
    else :
        odd_sum = odd_sum + num
    i = i +1

print (even_sum)
print (odd_sum)