element =[1,2,3,4,5,6,7,8,9,10]

""" x=0
c = []

for i in element[ : -2]:
    index_i = element.index(i)
    for j in element[index_i+1:-1]:
        index_j = element.index(j)
        for k in element[index_j+1: ]:
            c =(i,j,k)
            c.append(c)
            x = x+1
print(x)            
 """

ls=list(enumerate(element))
C = []

for (ni,i) in ls[ : -2]:
    for (nj,j) in ls[ni+1:-1]:
        for (nk,k) in ls[nj+1: ]:
            c =(i,j,k)
            C.append(c)

len(C)
print(C)