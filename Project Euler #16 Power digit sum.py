# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())

for i in range(num):
    sample = int(input())
    result = str(2**sample)
    number_list = list(map(int, list(result)))
    print(sum(number_list))
