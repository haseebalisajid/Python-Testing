i=int(input("enter number:"))
strnum=str(i)
y=0
x=len(strnum)
for ch in strnum:
    z=int(ch)
    a=z**x
    y=y+a
if y==i:
    print(i,"is an armstrong number")
else:
    print(i,"is not an armstrong number")



