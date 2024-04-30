l=[1,2,3,4,5,6,7,8,9]
length=len(l)
new_l=[]
i=0
k=3
sum=0
while i<length:
    for j in range(0,k):
        sum+=l[i]
        i+=1
    new_l.append(sum)
    sum=0
print(new_l)