# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.



def sumOfMultiples(min, max):
    sum = 0
    
    for i in range(min, max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

def sumOfMultRec(i, sum, max):

    if i >= max + 1: 
            return sum

    print(i)
        
    if i % 3 == 0 or i % 5 == 0:
        return sumOfMultRec(i+1, sum + i, max)


#s = sumOfMultiples(0, 1000)
s = sumOfMultRec(0, 0, 1000)

print(s) #233168 is the solution
