List=[4,6,2,7,8,3]
for k in range(len(List)+1):
    for i in range(len(List)-1):
        if List[i] > List[i+1]:
            List[i],List[i+1]= List[i+1],List[i]
print(List)
