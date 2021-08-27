#sum of first n prime numbers using loop
n = int(input("enter a number"))
sum = 0
num = 2
count = 0
while count < n:
    i = 2

    while i<=num: #check num is prime or not
    #for i in range(2, num+1):
        if ((num%i) == 0) and (i!=num):
            break

        if (i == num) or (num==2):
            sum = int(sum) + int(num)
            count += 1

        i += 1
    num += 1
print("sum of prime numbers:", sum)

