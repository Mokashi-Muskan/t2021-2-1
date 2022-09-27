n=int(input("Enter the value of a:"))
arr=[]
for i in range(100):
    if(i%2!=0):
        arr.append(i)
for i in range(n):
    print(arr[i],end=' ')