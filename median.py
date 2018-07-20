def median(List):
    sort_list=sorted(List)
    ist_step=len(sort_list)
    if ist_step%2 !=0:
        tnd_step=int(ist_step/2)
        median=sort_list[tnd_step]
        return median
    else:
        tnd_step=int(ist_step/2)
        scnd_step=sort_list[tnd_step]+sort_list[tnd_step-1]
        median=scnd_step/2
        return median
List=[5,2,3,1,4]
print(median(List))
