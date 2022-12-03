def fibonacci(n):
    '''
    the fibonacci function is call it self to build a solution
    The function should have one parameter n. The function should return the nth value in the fibonacci series.
    '''

    # fibonacci series starting with the integers 0 and 1.
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n >=2:
        return fibonacci(n-1) + fibonacci(n-2)
# the normal solve for fibonacci method solve is very slow
# becuase that this solution is better:

def fibonacci_other(n):

    '''
    The function should have one parameter n. The function should return the nth value in the fibonacci series.
    '''

    dir = {0:0 , 1:1}

    for i in range(2, n+1):

        dir[i] = dir[i-1] + dir[i-2]

    return (dir[n])



def lucas(n):

    '''
    The function should have one parameter n. The function should return the nth value in the lucas series.
    '''

    if n == 0:
        return 2
    if n == 1:
        return 1

    if n >=2:
        return lucas(n-1) + lucas(n-2)

def sum_series(n,v1=0,v2=1):

    '''
    this function returns the nth value
    n: The required parameter will determine which element in the series to print in the fibonacci or lucas series
    v1,v2: The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced (fibonacci or lucas).
    '''

    if v1 == 0 and v2 == 1 :
        return fibonacci(n)

    if v1 == 2 and v2 == 1 :
        return lucas(n)

print (fibonacci(4)) # 3 # this call fibonacci fun.
print (sum_series(4)) #3 # this call fibonacci fun.
print (fibonacci_other(4)) #3
print (sum_series(4,2,1)) #7