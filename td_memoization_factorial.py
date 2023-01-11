# TOP DOWN APPROACH
# #include<stdio.h>

# int Fibonacci(int N)
# {
#     if(N <= 1)
#         return N;
#     return Fibonacci(N-1) + Fibonacci(N-2);
# }

# int main()
# {
#     int n;
#     scanf("%d",&n);
#     printf("Fib(%d) = %d\n",n,Fibonacci(n));

#     return 0;
# }
import time
t0 = time.time()
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(9))
print("time taken =", time.time()-t0)
# above code is without memoization. 
# Suppose for n = 4, first left expression evaulates 
#                                 fib(4)
#               fib(3)[2]          +           fib(2)[1]
#         fib(2)[1] + fib(1)[1]              fib(1)[1] + fib(0)[0]
#   fib(1)+fib(0)[1+0]
# repetitive = fib(2)
# We can save the results of the fib(x) in an array and whenever next time the same 
# operation is asked , we directly fetch from stored value

# each array location shows the number to be evaluated , hence I dont need a dict :O

t1 = time.time()
n = 20
l = []
for i in range(n):
    l.append(-1) # tells that the num needs to be evaluated

def fib(n):
    if l[n] == -1:
        if n <= 1:
            return n
        else:
            l[n] = fib(n-1) + fib(n-2)
    return l[n]

print(fib(9))
print("New time=", time.time()-t1)


# LOOK AT THE TIME DIFFERENCE- WHEN n = 9
# As th number increases, the memoiztion gets better
# time taken = 6.031990051269531e-05

# New time= 1.621246337890625e-05