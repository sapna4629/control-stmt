print('code started')

def main():
    n= int(input('enter the number:'))
    a= int(input('enter the first number:'))
    d= int(input('enter the commom difference:'))
    res= factorial(n)
    sum= sum_natural_num(n,a,d)
    display(sum, res, n)

def sum_natural_num(n,a,d):
    sum= n//2* (2*a+ (n-1)* d)
    return sum
    
def factorial(n):
    if n==0:
        return 1
    
    else:
        return n* factorial(n-1)
    

def display(sum, res, n):
    print(f' the sum of number is {sum} and the multiple of natural number is {res}')

main()
print('code ended')


