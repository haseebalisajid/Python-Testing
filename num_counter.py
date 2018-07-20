def count(sequence,item):
    sumx=0
    for i in List:
        if i==item:
            sumx+=1
        else:
            sumx=sumx
    return sumx
List=[]
x=int(input("how many inputs you want to put:"))
while x>=1:
    y=int(input("enter sequence:"))
    List.append(y)
    x-=1
item=int(input("enter item:"))
print(count(List,item))
