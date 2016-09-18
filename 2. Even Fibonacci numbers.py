max = 4000000


def even(a):
    if a % 2 == 0:
        return 1
    return 0



def fibEvenNums(a,b,s):

    c = a + b

    if c > max:
        print(s)
        return

    if even(c):
        print( c )
        s += c
        
    fibEvenNums(b, c, s)

fibEvenNums(1,2, 2)



