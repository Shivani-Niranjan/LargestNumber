'''
Given an array A of non-negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Input 1:
A = [3, 30, 34, 5, 9]

Input 2:
A = [2, 3, 9, 0]

Output 1:
"9534330"

Output 2:
"9320"
'''

def largestNumber(A):
    A = list(map(str, A))  # Convert each number to a string
    
    def compare(x, y):
        return int(x + y) - int(y + x)
    
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if compare(A[i], A[j]) < 0:
                A[i], A[j] = A[j], A[i]
    
    return "".join(A)

array = list(map(int, input().split()))
print(largestNumber(array)) 
