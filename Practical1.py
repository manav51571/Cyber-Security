categorie=3
chef=3
c=[]
b=[0,0,0]
for i in range(chef):         
    a =[]
    print('Enter score for chef',i,'between 0 to 100:-')
    for j in range(categorie):      
         a.append(int(input()))
    c.append(a)
a=0
for j in range(categorie):
    a=0
    for i in range(chef):
        if i == 0:
            a=0
        else:
            if c[a][j] < c[i][j]:
                a=i
            elif c[a][j] > c[i][j]:
                a=a
            else:
                a=-1
    if a >= 0:
        b[a]=b[a]+1   
for i in range(0,chef):
    print('Chef',i+1,' Points = ',b[i])