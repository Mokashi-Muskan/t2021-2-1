n=int(input())
arr=[]
for i in range(100):
    if(i%2!=0):
        arr.append(i)
if(n==1 or n==2):
    print("1")
else:
    for i in range(n):
        print(arr[i])
f