# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())

def factorial(number):
    factorial_result = 1
    if number==1:
        pass
    else:
        for i in range(number,0,-1):
            factorial_result*=i
            
    return factorial_result

for i in range(num):
    factorial_num = int(input())
    result=factorial(factorial_num)
    num_list = list(map(int, list(str(result))))
    print(sum(num_list))
    
    
