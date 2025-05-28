X,Y=map(int,input().split())

count=0

for a in range(1,7):
    for b in range(1,7):
        if a+b>=X or a+Y<=b or b+Y<=a:
            count+=1



print(count/36)