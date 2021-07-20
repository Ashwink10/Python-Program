num=int(input("Enter a range number:"))
a=0
b=1
sum1=0
count=1
print("Fibonacci series\n")
while (count<num):
    print(a)
    sum1=a+b
    a=b
    b=sum1
    count+=1
    